import pathlib
import re
from tqdm.notebook import tqdm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy.signal import medfilt
import math
import yaml
from typing import Tuple
from typing import List

import continuous_peak_fit_analysis_functions as analysis
import continuous_peak_fit_deformation_functions as deformation

def extract_sxrd_input(config_path: str):
    """Extract user inputs from yaml configuration file. 
    Extract additional inputs for deformation experiments,
    (including deformation start and end numbers), as well 
    as input and output file paths, peak labels, data 
    resolution and image numbers. These inputs are used
    to calculate the intensity values from .fit files.
    
    :param config_path: path to the configuration file.
    
    :return: experiment number, input path for the .fit file, 
    lattice plane peak labels, data resolution, image numbers,
    as well as the path for the thermomechanical data during deformation, 
    the start and end of deformation, the acquisition frequency
    of SXRD images and deformation data, the output file path, 
    and if it is needed the file path for data recorded from the analogue 
    output, including conversions for load, temperature and position.
    - as strings, integers and a list of integers.
    """
    config = analysis.get_config(config_path)
    
    beam_energy = config["deformation_input"]["beam_energy"]
    print("The beam energy (in keV) is:", beam_energy, sep='\n', end='\n\n')
    
    azimuth_load_direction = config["deformation_input"]["azimuth_load_direction"]
    print("The load direction along the azimuthal angle (in degrees) is:", beam_energy, sep='\n', end='\n\n')
    
    filter_sxrd = config["deformation_input"]["filter_sxrd"]
    print("A median filter is being applied to the SXRD data, with a value of:", filter_sxrd, sep='\n', end='\n\n')
    
    return beam_energy, azimuth_load_direction, filter_sxrd

def colour_range(N: int = 9, colour_map: str = 'viridis'):
    """ Return a range of hex colour codes for a particular colour map.
    
    :param N: number of desired colour codes (default is 9).
    :param colour_map: type of colour map (default is 'viridis').
    :return: list of hex colour codes
    """
    base = plt.cm.get_cmap(colour_map)
    colour_list = base(np.linspace(0, 1, N))
    colour_hex_list=[]
    for i in range (N-1, -1, -1):
         colour_hex_list.append(colors.rgb2hex(colour_list[i]))
    
    return colour_hex_list

def colour_assign(peak_label: list, alpha_colour_type: str = "viridis", beta_colour_type: str = "PuRd"):
    alpha_peak_label = []
    beta_peak_label = []
    
    for i in range(len(peak_label) - 1):
        if(len(peak_label[i]) >= 4):
            alpha_peak_label += [peak_label[i]]
        elif(len(peak_label[i]) < 4):
            beta_peak_label += [peak_label[i]]
            
    alpha_colour = colour_range(len(alpha_peak_label), alpha_colour_type)
    beta_colour = colour_range(len(beta_peak_label), beta_colour_type)
    
    plane_colour = dict()
    
    for label, colour in zip(alpha_peak_label, alpha_colour):
        plane_colour[label] = colour
    
    for label, colour in zip(beta_peak_label, beta_colour):
        plane_colour[label] = colour
        
    print("Plane colours have been defined for ", len(plane_colour), " lattice planes.", end='\n\n')
        
    return plane_colour

def marker_assign(peak_label):
    alpha_peak_label = []
    beta_peak_label = []
    
    for i in range(len(peak_label) - 1):
        if(len(peak_label[i]) >= 4):
            alpha_peak_label += [peak_label[i]]
        elif(len(peak_label[i]) < 4):
            beta_peak_label += [peak_label[i]] 
            
    # define alpha markers        
    alpha_marker = ['s','H','^','v','D','<','d','*','o','h','>','p', 's','H','^','v','D','<','d','*','o','h','>','p'] 
    
    # define beta markers, dependant on 211 peak
    beta_marker = ['+','x','P','|','-']
    for label in beta_peak_label:
        if label == '(211)':
            print("Beta (211) lattice plane peak has been found and included as a marker.")
            # add extra cross (filled) for 211 peak
            beta_marker = ['+','x','X','P','|','-', '+','x','X','P','|','-']
    
    plane_marker = dict()
    
    for label, marker in zip(alpha_peak_label, alpha_marker):
        plane_marker[label] = marker
    
    for label, marker in zip(beta_peak_label, beta_marker):
        plane_marker[label] = marker
        
    print("Plane markers have been defined for ", len(plane_marker), " lattice planes.", end='\n\n')
    
    return plane_marker

def calc_dspacing(two_theta: float, x_ray_energy: float = 89.07) -> float:
    """ Calculate d-spacing from 2-theta values using Bragg's law.
    
    :param two_theta: 2-theta value in degrees.
    :param x_ray_energy: X-ray energy in keV (default is 89.07 keV).
    :return: d-spacing in metres.
    """ 
    c = 2.99792458e8
    h = 6.62607004e-34
    e = 1.6021766208e-19
    x_ray_wavelength = (h * c) / (x_ray_energy * 1e3 * e)
    dspacing = x_ray_wavelength / (2 * np.sin(np.array(two_theta) * np.pi / 360))
    
    return dspacing

def calc_strain(two_theta: np.ndarray, zero_range: int = 1) -> np.ndarray:
    """ Calculate strain from 2-theta values.
    
    :param two_theta: 2-theta value in degrees.
    :param zero_range: Integer used to define a range of points to calculate an average initial 2-theta value
                       (default is 1).
    :return: NumPy array of strain values in degrees.
    """ 
    two_theta = 0.5 * (np.array(two_theta)) * np.pi / 180.0
    two_theta_0 = np.mean(two_theta[0:zero_range])
    print(two_theta_0)
    strain = - (two_theta - two_theta_0) / np.tan(two_theta)
    
    return strain

def relative_amplitude(amplitude: np.ndarray) -> np.ndarray:
    """ Divide an array of amplitude values by the first value in the array.
    
    :param amplitude: NumPy array of amplitude float values.
    :return: NumPy array of float values.
    """ 
    relative_amplitude = np.array(amplitude) / amplitude[0]
    
    return relative_amplitude

def find_start_end_microstrain(start_number: int, end_number: int, image_numbers: list, peak_label: list, peak_position_time: dict, plane_colour: dict, plane_marker: dict):

    # match the start and end numbers to values and indices in the arrays
    start_value, start_index, end_value, end_index = deformation.match_array_numbers(image_numbers, start_number, end_number)

    print("Adjust the start and end image number values until you only capture the deforming region, where there will be a characteristic response observed in the lattice microstrain.")
          
    # use the start and end indices to plot microstrain versus frame number
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    for peak in peak_label:
        peak_position_time_array = np.array(peak_position_time[peak][0])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        plt.plot(image_numbers[start_index:end_index], microstrain, marker=plane_marker[peak], 
                 color=plane_colour[peak], markersize=1, label=peak)
        plt.legend(fontsize = 20)
        plt.ylabel("Lattice Microstrain", fontsize = 20)
        plt.xlabel("Frame Number", fontsize = 20)
        
    plt.show()

def follow_azimuth_angle(peak_position, image_numbers, start_number, end_number,
                         peak_label, data_resolution, plane_colour, plane_marker, output_file_path, experiment_number):
    # create list of azimuthal degree
    azimuth_degree = list(range(0, 360, data_resolution))
    
    max_azimuth = dict()
    min_azimuth = dict()
    
    for label in peak_label:
        
        max_azimuth[label] = np.zeros(len(peak_position[label][0]))
        min_azimuth[label] = np.zeros(len(peak_position[label][0]))
        
        for image_number in range(len(peak_position[label][0])):

            max_position = 0
            min_position = 100

            for azimuth in azimuth_degree:

                position = peak_position[label][azimuth][image_number]

                if(position > max_position):
                    max_azimuth[label][image_number] = azimuth
                    max_position = position

                if(position < min_position):
                    min_azimuth[label][image_number] = azimuth
                    min_position = position
    
    # match the start and end numbers to values and indices in the arrays
    start_value, start_index, end_value, end_index = deformation.match_array_numbers(image_numbers, start_number, end_number)
    
    # plot the variation in the azimuthal angle of the maximum position of the ring
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    print("Variation of azimuthal angle of the maximum position of the ring:")
    for peak in peak_label:
        plt.plot(image_numbers[start_index:end_index], max_azimuth[peak][start_index:end_index], marker=plane_marker[peak], color=plane_colour[peak], markersize=1, label=peak)
        plt.legend(fontsize = 20)
        plt.ylabel(r"Azimuthal Angle, ${\nu}$ ${(^\circ C)}$", fontsize = 20)
        plt.xlabel("Image Number", fontsize = 20)
     
    plt.tight_layout()
    output_folder = output_file_path.format(experiment_number = experiment_number)
    plt.savefig("{output_folder}/max_azimuth_{experiment_number}.png".format(output_folder = output_folder,  
                                                                             experiment_number = experiment_number))
    plt.show()
    
    # plot the variation in the azimuthal angle of the minimum position of the ring
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    print("Variation of azimuthal angle of the minimum position of the ring:")
    for peak in peak_label:
        plt.plot(image_numbers[start_index:end_index], min_azimuth[peak][start_index:end_index], marker=plane_marker[peak], color=plane_colour[peak], markersize=1, label=peak)
        plt.legend(fontsize = 20)
        plt.ylabel(r"Azimuthal Angle, ${\nu}$ ${(^\circ C)}$", fontsize = 20)
        plt.xlabel("Image Number", fontsize = 20)
     
    plt.tight_layout()
    output_folder = output_file_path.format(experiment_number = experiment_number)
    plt.savefig("{output_folder}/min_azimuth_{experiment_number}.png".format(output_folder = output_folder,  
                                                                             experiment_number = experiment_number))
    plt.show()