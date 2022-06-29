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
    print("The load direction along the azimuthal angle (in degrees) is:", azimuth_load_direction, sep='\n', end='\n\n')
    
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

def find_start_end_microstrain(start_number: int, end_number: int, image_numbers: list, peak_position_time: dict, peak_label: list, azimuth_load_direction: int, plane_colour: dict, plane_marker: dict):

    # match the start and end numbers to values and indices in the arrays
    start_value, start_index, end_value, end_index = deformation.match_array_numbers(image_numbers, start_number, end_number)

    print("Adjust the start and end image number values until you only capture the deforming region, where there will be a characteristic response observed in the lattice microstrain.")
          
    # use the start and end indices to plot microstrain versus frame number
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    for peak in peak_label:
        peak_position_time_array = np.array(peak_position_time[peak][azimuth_load_direction])
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
    
    # plot the variation in the azimuthal angle of the maximum and minimum position of the ring
    print("Variation of azimuthal angle of the MAXIMUM and MINIMUM position of the ring:")
    fig,((ax1),(ax2)) = plt.subplots(2, 1, figsize=(20,10))

    for peak in peak_label:
        ax1.plot(image_numbers[start_index:end_index], max_azimuth[peak][start_index:end_index], marker=plane_marker[peak], color=plane_colour[peak], markersize=1, label=peak)
        ax1.set_xlabel("Image Number", fontsize = 20)
        ax1.set_ylabel(r"Azimuthal Angle, ${\nu}$ ${(^\circ C)}$", fontsize = 20)
        ax1.legend(fontsize = 20)
        ax1.set_title(r"Maximum ${2 \theta}$ / Minimum d-spacing", fontsize = 20)

        ax2.plot(image_numbers[start_index:end_index], min_azimuth[peak][start_index:end_index], marker=plane_marker[peak], color=plane_colour[peak], markersize=1, label=peak)
        ax2.set_xlabel("Image Number", fontsize = 20)
        ax2.set_ylabel(r"Azimuthal Angle, ${\nu}$ ${(^\circ C)}$", fontsize = 20)
        ax2.legend(fontsize = 20)
        ax2.set_title(r"Minimum ${2 \theta}$ / Maximum d-spacing", fontsize = 20)
     
    plt.tight_layout()
    output_folder = output_file_path.format(experiment_number = experiment_number)
    plt.savefig("{output_folder}/max_min_azimuth_{experiment_number}.png".format(output_folder = output_folder,  
                                                                             experiment_number = experiment_number))
    plt.show()
    
def plot_microstrain_stress(start_number: int, end_number: int, image_numbers: list,
                            peak_position_time: dict, true_stress: np.ndarray, 
                            peak_label: list, azimuth_load_direction: int, plane_marker: dict, plane_colour: dict, 
                            output_file_path: str, experiment_number: int, filter_data: int = 1,
                            number_of_points: int = 50, microstrain_limit: float = 0, true_stress_limit: float = 0):
    
    """ Plot load, temperature and position data, from instrument data recorded for each diffraction pattern image.
    The instrument data is in the form of an analogue voltage signal, with a conversion factor used to calculate 
    the Newtons, Degree Celsius or Millimetre values to plot.
    
    :param file_path_instrument_data: input file path string.
    :param start_deform: value defining the start point of deformation.
    :param end_deform: value defining the end point of deformation.
    :param load_conversion: conversion for load in Newton / Volt (default is 25).
    :param temp_conversion: conversion for temperature in Degree Celsius / Volt (default is 150).
    :param position_conversion: conversion for position in Millimetres / Volt  (default is 0.5).
    
    :return: length of the instrument data (equivalent to the maximum frame).
    """
    # set the output folder
    output_folder = output_file_path.format(experiment_number = experiment_number)
    
    # match the start and end numbers to values and indices in the arrays
    start_value, start_index, end_value, end_index = deformation.match_array_numbers(image_numbers, start_number, end_number)
    
    # set number of points to be plotted
    if number_of_points == 0:
        number_of_points = end_index - start_index
    else:
        number_of_points = number_of_points
    
    # set initial limits applied to false
    limits_applied = False
    
    # plot the lattice microstrain variation with applied true stress for four different orthogonal directions
    print("Lattice microstrain variation with applied true stress for four different orthogonal directions:")
    
    fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2, 2, figsize=(20,10))

    for peak in peak_label:

        peak_position_time_array = np.array(peak_position_time[peak][0])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax1.plot(microstrain[0:number_of_points],true_stress[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax1.set_xlabel('Microstrain', fontsize=20)
        ax1.set_ylabel('True Stress, ${\sigma}$, (MPa)', fontsize = 20)
        ax1.minorticks_on()
        ax1.legend()
        ax1.set_title(r'${0^\circ}$', fontsize = 20)

        peak_position_time_array = np.array(peak_position_time[peak][90])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax2.plot(microstrain[0:number_of_points],true_stress[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax2.set_xlabel('Microstrain', fontsize=20)
        ax2.set_ylabel('True Stress, ${\sigma}$, (MPa)', fontsize = 20)
        ax2.minorticks_on()
        ax2.legend()
        ax2.set_title(r'${90^\circ}$', fontsize = 20)

        peak_position_time_array = np.array(peak_position_time[peak][180])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax3.plot(microstrain[0:number_of_points],true_stress[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax3.set_xlabel('Microstrain', fontsize=20)
        ax3.set_ylabel('True Stress, ${\sigma}$, (MPa)', fontsize = 20)
        ax3.minorticks_on()
        ax3.legend()
        ax3.set_title(r'${180^\circ}$', fontsize = 20)

        peak_position_time_array = np.array(peak_position_time[peak][270])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax4.plot(microstrain[0:number_of_points],true_stress[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax4.set_xlabel('Microstrain', fontsize=20)
        ax4.set_ylabel('True Stress, ${\sigma}$, (MPa)', fontsize = 20)
        ax4.minorticks_on()
        ax4.legend()
        ax4.set_title(r'${270^\circ}$', fontsize = 20)

        if microstrain_limit > 0:
            ax1.set_xlim([0, microstrain_limit])
            ax2.set_xlim([0, microstrain_limit])
            ax3.set_xlim([0, microstrain_limit])
            ax4.set_xlim([0, microstrain_limit])
            limits_applied = True

        if microstrain_limit < 0 :
            ax1.set_xlim([microstrain_limit, 0])
            ax2.set_xlim([microstrain_limit, 0])
            ax3.set_xlim([microstrain_limit, 0])
            ax4.set_xlim([microstrain_limit, 0])
            limits_applied = True

        if true_stress_limit > 0:
            ax1.set_ylim([0, true_stress_limit])
            ax2.set_ylim([0, true_stress_limit])
            ax3.set_ylim([0, true_stress_limit])
            ax4.set_ylim([0, true_stress_limit])
            limits_applied = True

        if true_stress_limit < 0 :
            ax1.set_ylim([true_stress_limit, 0])
            ax2.set_ylim([true_stress_limit, 0])
            ax3.set_ylim([true_stress_limit, 0])
            ax4.set_ylim([true_stress_limit, 0])
            limits_applied = True

    plt.tight_layout()
    
    if limits_applied: 
        plt.savefig("{output_folder}/microstrain_true_stress_limited_{experiment_number}.png".format(
                                                                                output_folder = output_folder, 
                                                                                experiment_number = experiment_number))
    elif not limits_applied:
        plt.savefig("{output_folder}/microstrain_true_stress_{experiment_number}.png".format(
                                                                                output_folder = output_folder, 
                                                                                experiment_number = experiment_number))
    plt.show()

    # plot the lattice microstrain variation with applied true stress in the chosen loading direction
    print(f"Lattice microstrain variation with applied true stress in chosen loading direction, defined at an azimuthal angle of '{azimuth_load_direction}' degrees:", end='\n\n')
    
    # create dictionary for saving lattice microstrain
    microstrain_write = dict()
    
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    
    for peak in peak_label:
        
        peak_position_time_array = np.array(peak_position_time[peak][azimuth_load_direction])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        microstrain_write[peak] = microstrain[0:number_of_points]
        
        plt.plot(microstrain[0:number_of_points],true_stress[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        plt.legend(fontsize=20)
        plt.xlabel('Microstrain', fontsize = 20)
        plt.ylabel('True Stress, ${\sigma}$, (MPa)', fontsize = 20)
        plt.tight_layout()
        
        if microstrain_limit > 0:
            plt.xlim([0, microstrain_limit])
            limits_applied = True
            
        if microstrain_limit < 0 :
            plt.xlim([microstrain_limit, 0])
            limits_applied = True
            
        if true_stress_limit > 0:
            plt.ylim([0, true_stress_limit])
            limits_applied = True
            
        if true_stress_limit < 0 :
            plt.ylim([true_stress_limit, 0])
            limits_applied = True
        
    if limits_applied:
        plt.savefig("{output_folder}/microstrain_true_stress_load_direction_limited_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,  
                                                                                 experiment_number = experiment_number))
    elif not limits_applied:
        plt.savefig("{output_folder}/microstrain_true_stress_load_direction_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,  
                                                                                 experiment_number = experiment_number))
    plt.show()
    
    # define the true stress for writing out
    true_stress_write = true_stress[0:number_of_points]
    
    # open a file to save the microstrain measurements
    output_text_path =  "{output_folder}/microstrain_true_stress_load_direction_{experiment_number}.txt".format(
                                                                             output_folder = output_folder,  
                                                                             experiment_number = experiment_number)
    output_text_folder = pathlib.Path(output_text_path).parent
    output_text_folder.mkdir(exist_ok=True)

    with open(output_text_path, 'w') as output_file:
        
        output_file.write(f"True Stress \t")
        
        for peak in peak_label:
            # write lattice plane peak labels at top of file
            output_file.write(f"{peak} Microstrain \t")
        
        output_file.write(f"\n")
        
        # write true stress and microstrain values
        for i in range(len(true_stress_write)):
            output_file.write(f"{true_stress_write[i]}\t")
            for peak in peak_label:
                output_file.write(f"{microstrain_write[peak][i]}\t")
            output_file.write(f"\n")
            
    number_of_peaks = len(peak_label)        
    print(f"The lattice microstrain for '{number_of_peaks}' peaks has been saved to a .txt file: '{output_text_path}'.")
    
def plot_microstrain_strain(start_number: int, end_number: int, image_numbers: list,
                            peak_position_time: dict, true_strain: np.ndarray, 
                            peak_label: list, azimuth_load_direction: int, plane_marker: dict, plane_colour: dict, 
                            output_file_path: str, experiment_number: int, filter_data: int = 1,
                            number_of_points: int = 0, microstrain_limit: float = 0, true_strain_limit: float = 0):
    
    """ Plot load, temperature and position data, from instrument data recorded for each diffraction pattern image.
    The instrument data is in the form of an analogue voltage signal, with a conversion factor used to calculate 
    the Newtons, Degree Celsius or Millimetre values to plot.
    
    :param file_path_instrument_data: input file path string.
    :param start_deform: value defining the start point of deformation.
    :param end_deform: value defining the end point of deformation.
    :param load_conversion: conversion for load in Newton / Volt (default is 25).
    :param temp_conversion: conversion for temperature in Degree Celsius / Volt (default is 150).
    :param position_conversion: conversion for position in Millimetres / Volt  (default is 0.5).
    
    :return: length of the instrument data (equivalent to the maximum frame).
    """
    # set the output folder
    output_folder = output_file_path.format(experiment_number = experiment_number)
    
    # match the start and end numbers to values and indices in the arrays
    start_value, start_index, end_value, end_index = deformation.match_array_numbers(image_numbers, start_number, end_number)
    
    # set number of points to be plotted
    if number_of_points == 0:
        number_of_points = end_index - start_index
    else:
        number_of_points = number_of_points
        
    # set initial limits applied to false
    limits_applied = False
    
    # plot the lattice microstrain variation with applied true strain for four different orthogonal directions
    print("Lattice microstrain variation with applied true strain for four different orthogonal directions:")

    fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2, 2, figsize=(20,10))

    for peak in peak_label:

        peak_position_time_array = np.array(peak_position_time[peak][0])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax1.plot(true_strain[0:number_of_points],microstrain[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax1.set_xlabel('True Strain, ${\epsilon}$, (MPa)', fontsize = 20)
        ax1.set_ylabel('Microstrain', fontsize=20)
        ax1.minorticks_on()
        ax1.legend()
        ax1.set_title(r'${0^\circ}$', fontsize = 20)

        peak_position_time_array = np.array(peak_position_time[peak][90])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax2.plot(true_strain[0:number_of_points],microstrain[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax2.set_xlabel('True Strain, ${\epsilon}$, (MPa)', fontsize = 20)
        ax2.set_ylabel('Microstrain', fontsize=20)
        ax2.minorticks_on()
        ax2.legend()
        ax2.set_title(r'${90^\circ}$', fontsize = 20)

        peak_position_time_array = np.array(peak_position_time[peak][180])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax3.plot(true_strain[0:number_of_points],microstrain[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax3.set_xlabel('True Strain, ${\epsilon}$, (MPa)', fontsize = 20)
        ax3.set_ylabel('Microstrain', fontsize=20)
        ax3.minorticks_on()
        ax3.legend()
        ax3.set_title(r'${180^\circ}$', fontsize = 20)

        peak_position_time_array = np.array(peak_position_time[peak][270])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        ax4.plot(true_strain[0:number_of_points],microstrain[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        ax4.set_xlabel('True Strain, ${\epsilon}$, (MPa)', fontsize = 20)
        ax4.set_ylabel('Microstrain', fontsize=20)
        ax4.minorticks_on()
        ax4.legend()
        ax4.set_title(r'${270^\circ}$', fontsize = 20)

        if true_strain_limit > 0:
            ax1.set_xlim([0, true_strain_limit])
            ax2.set_xlim([0, true_strain_limit])
            ax3.set_xlim([0, true_strain_limit])
            ax4.set_xlim([0, true_strain_limit])
            limits_applied = True

        if true_strain_limit < 0 :
            ax1.set_xlim([true_strain_limit, 0])
            ax2.set_xlim([true_strain_limit, 0])
            ax3.set_xlim([true_strain_limit, 0])
            ax4.set_xlim([true_strain_limit, 0])
            limits_applied = True
        
        if microstrain_limit > 0:
            ax1.set_ylim([0, microstrain_limit])
            ax2.set_ylim([0, microstrain_limit])
            ax3.set_ylim([0, microstrain_limit])
            ax4.set_ylim([0, microstrain_limit])
            limits_applied = True

        if microstrain_limit < 0 :
            ax1.set_ylim([microstrain_limit, 0])
            ax2.set_ylim([microstrain_limit, 0])
            ax3.set_ylim([microstrain_limit, 0])
            ax4.set_ylim([microstrain_limit, 0])
            limits_applied = True

    plt.tight_layout()
    
    if limits_applied: 
        plt.savefig("{output_folder}/true_strain_microstrain_limited_{experiment_number}.png".format(
                                                                                output_folder = output_folder, 
                                                                                experiment_number = experiment_number))
    elif not limits_applied:
        plt.savefig("{output_folder}/true_strain_microstrain_{experiment_number}.png".format(
                                                                                output_folder = output_folder, 
                                                                                experiment_number = experiment_number))
    plt.show()

    # plot the lattice microstrain variation with applied true strain in the chosen loading direction
    print(f"Lattice microstrain variation with applied true strain in chosen loading direction, defined at an azimuthal angle of '{azimuth_load_direction}' degrees:", end='\n\n')
    
    # create dictionary for saving lattice microstrain
    microstrain_write = dict()
    
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    
    for peak in peak_label:
        
        peak_position_time_array = np.array(peak_position_time[peak][azimuth_load_direction])
        microstrain = calc_strain(peak_position_time_array[start_index:end_index])*1e6
        microstrain = medfilt(microstrain,filter_data)
        microstrain_write[peak] = microstrain[0:number_of_points]
        
        plt.plot(true_strain[0:number_of_points],microstrain[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        plt.legend(fontsize=20)
        plt.xlabel('True Strain, ${\epsilon}$, (MPa)', fontsize = 20)
        plt.ylabel('Microstrain', fontsize = 20)
        plt.tight_layout()
        
        if true_strain_limit > 0:
            plt.xlim([0, true_strain_limit])
            limits_applied = True
            
        if true_strain_limit < 0 :
            plt.xlim([true_strain_limit, 0])
            limits_applied = True
        
        if microstrain_limit > 0:
            plt.ylim([0, microstrain_limit])
            limits_applied = True
            
        if microstrain_limit < 0 :
            plt.ylim([microstrain_limit, 0])
            limits_applied = True
        
    if limits_applied:
        plt.savefig("{output_folder}/true_strain_microstrain_load_direction_limited_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,  
                                                                                 experiment_number = experiment_number))        
    elif not limits_applied: 
        plt.savefig("{output_folder}/true_strain_microstrain_load_direction_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,  
                                                                                 experiment_number = experiment_number))
    plt.show()
    
    # define the true stress for writing out
    true_strain_write = true_strain[0:number_of_points]
    
    # open a file to save the microstrain measurements
    output_text_path =  "{output_folder}/true_strain_microstrain_load_direction_{experiment_number}.txt".format(
                                                                             output_folder = output_folder,  
                                                                             experiment_number = experiment_number)
    output_text_folder = pathlib.Path(output_text_path).parent
    output_text_folder.mkdir(exist_ok=True)

    with open(output_text_path, 'w') as output_file:
        
        output_file.write(f"True Strain \t")
        
        for peak in peak_label:
            # write lattice plane peak labels at top of file
            output_file.write(f"{peak} Microstrain \t")
        
        output_file.write(f"\n")
        
        # write true stress and microstrain values
        for i in range(len(true_strain_write)):
            output_file.write(f"{true_strain_write[i]}\t")
            for peak in peak_label:
                output_file.write(f"{microstrain_write[peak][i]}\t")
            output_file.write(f"\n")
            
    number_of_peaks = len(peak_label)        
    print(f"The lattice microstrain for '{number_of_peaks}' peaks has been saved to a .txt file: '{output_text_path}'.")