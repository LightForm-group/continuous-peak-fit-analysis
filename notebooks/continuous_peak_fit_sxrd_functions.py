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
    Extract additional inputs for synchrotron analysis,
    including beam energy, azimuthal load direction, and medium
    filter, as well as number of points and limits for plotting.
    These inputs are used to plot the synchrotron peak fit data 
    with the thermomechanical data.
    
    :param config_path: path to the configuration file.
    
    :return: beam energy, azimuthal load direction, number of
    points to plot for stress and strain plots, limits for the 
    stress, strain, microstrain, full width half maximum (FWHM), 
    intensity, relative intensity, intensity*FWHM, and relative intensity*FWHM.
    - as strings and integers.
    """
    config = analysis.get_config(config_path)
    
    beam_energy = config["deformation_input"]["beam_energy"]
    print("The beam energy (in keV) is:", beam_energy, sep='\n', end='\n\n')
    
    azimuth_load_direction = config["deformation_input"]["azimuth_load_direction"]
    print("The load direction along the azimuthal angle (in degrees) is:", azimuth_load_direction, sep='\n', end='\n\n')
    
    filter_sxrd = config["deformation_input"]["filter_sxrd"]
    print("A median filter is being applied to the SXRD data, with a value of:", filter_sxrd, sep='\n', end='\n\n')
    
    number_of_points_stress = config["deformation_input"]["number_of_points_stress"]
    print("The number of points to plot against true stress (typically capturing elastic to plastic transition) is:", filter_sxrd, sep='\n', end='\n\n')
    
    number_of_points_strain = config["deformation_input"]["number_of_points_strain"]
    print("The number of points to plot against true strain is:", filter_sxrd, sep='\n', end='\n\n')
    
    true_stress_limit = config["deformation_input"]["true_stress_limit"]
    print("The plot limit for the true stress axis is:", true_stress_limit, sep='\n', end='\n\n')
    
    true_strain_limit = config["deformation_input"]["true_strain_limit"]
    print("The plot limit for the true strain axis is:", true_strain_limit, sep='\n', end='\n\n')
    
    microstrain_limit = config["deformation_input"]["microstrain_limit"]
    print("The plot limit for the microstrain axis is:", microstrain_limit, sep='\n', end='\n\n')
    
    FWHM_limit = config["deformation_input"]["FWHM_limit"]
    print("The plot limit for the Full Width Half Maximum (FWHM) axis is:", FWHM_limit, sep='\n', end='\n\n')
    
    intensity_limit = config["deformation_input"]["intensity_limit"]
    print("The plot limit for the intensity axis is:", intensity_limit, sep='\n', end='\n\n')
    
    relative_intensity_limit = config["deformation_input"]["relative_intensity_limit"]
    print("The plot limit for the relative intensity axis is:", microstrain_limit, sep='\n', end='\n\n')
    
    intensity_x_FWHM_limit = config["deformation_input"]["intensity_x_FWHM_limit"]
    print("The plot limit for the intensity * FWHM axis is:", microstrain_limit, sep='\n', end='\n\n')
    
    relative_intensity_x_FWHM_limit = config["deformation_input"]["relative_intensity_x_FWHM_limit"]
    print("The plot limit for the relative intensity * FWHM axis is:", microstrain_limit, sep='\n', end='\n\n')
    
    return beam_energy, azimuth_load_direction, filter_sxrd, number_of_points_stress, number_of_points_strain, true_stress_limit, true_strain_limit, microstrain_limit, FWHM_limit, intensity_limit, relative_intensity_limit, intensity_x_FWHM_limit, relative_intensity_x_FWHM_limit

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

def calc_relative_values(values: np.ndarray) -> np.ndarray:
    """ Divide an array of values by the first value in the array.
    
    :param values: NumPy array of float values.
    :return: NumPy array of float values.
    """ 
    relative_values = np.array(values) / values[0]
    
    return relative_values

def multiply_peak_params(peak_param_time_1, peak_param_time_2):
    peak_param_result = dict()
    """ Multiply two dictionaries of single peak data of specific lattice planes,
    at specific azimuthal angles, over time.
    
    :peak_param_time_1: dictionary of the peak parameter values for all lattice plane peaks, at all azimuthal angles, over time.
    :peak_param_time_1: dictionary of the peak parameter values for all lattice plane peaks, at all azimuthal angles, over time.
    :return: dictionary of the multiplied peak parameter values with same structure as input.
    """ 
    for label in peak_param_time_1.keys():
        peak_param_result[label] = dict() 
        for azimuth in peak_param_time_1[label]:
            peak_param_result[label][azimuth] = []
            for i in range(len(peak_param_time_1[label][azimuth])):
                multiply_result = peak_param_time_1[label][azimuth][i]*peak_param_time_2[label][azimuth][i]
                peak_param_result[label][azimuth].append(multiply_result)
    return peak_param_result

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
                                                                             experiment_number = experiment_number),
                                                                             facecolor='white')
    plt.show()
    
def plot_peak_param_stress(peak_param_type: str, start_number: int, end_number: int, image_numbers: list,
                           peak_param_time: dict, true_stress: np.ndarray, 
                           peak_label: list, azimuth_load_direction: int, plane_marker: dict, plane_colour: dict, 
                           output_file_path: str, experiment_number: int, filter_data: int = 1,
                           number_of_points: int = 50, peak_param_limit: float = 0, true_stress_limit: float = 0):
    
    """ Plot the macromechanical true stress response versus a micromechanical peak parameter feature (measured from 
    synchrotron diffraction), along different azimuthal directions, and along the loading direction. Current options for peak 
    parameter feature are Microstrain, Intensity and FWHM. Limits can be applied to constrain the plot and for consistency 
    with other plots. The plot data for the loading direction is also written to a text file.
    
    :param peak_param_type: a string defining the type of peak parameter e.g. Microstrain, Intensity, or FWHM
    :param start_number: a value defining the start point of deformation.
    :param end_number: a value defining the end point of deformation.
    :param image_numbers: a list of the diffraction pattern image numbers.
    :param peak_param_time: a dictionary of the peak parameter variation over time for different lattice plane peaks, along different directions.
    :param true_stress: an array of the true stress values already synchronised with the peak parameter variation.
    :param peak_label: a list of the lattice plane peak labels to plot.
    :param azimuth_load_direction: a value for the azimuthal angle of the loading direction.
    :param plane_marker: a dictionary of markers relating to the lattice plane peak labels.
    :param plane_colour: a dictionary of colours relating to the lattice plane peak labels.
    :param output_file_path: an output path for storing the results.
    :param experiment_number: an experiment number as reference for the test.
    :param filter_data: a value for a medium filter to smooth the synchrotron peak parameter data.
    :param number_of_points: a total number of peak parameter points to plot from the data.
    :param peak_param_limit: a peak parameter value limit for defining the maximum X bounds of the plot.
    :param true_stress_limit: a true stress value limit for defining the maximum Y bounds of the plot.
    
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
    
    # plot the peak parameter variation with applied true stress for four different orthogonal directions
    print(f"Lattice {peak_param_type} variation with applied true stress for four different orthogonal directions:")
    
    # define the number of subplots
    angles = [0, 90, 180, 270]
    n=2
    m=2
    fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(20,10))

    # plot the peak parameter data for each of the lattice planes
    for peak in peak_label:
        for i, ax in enumerate(axes.flatten()):
            angle = angles[i]
            peak_param_time_array = np.array(peak_param_time[peak][angle])
               
            # choose the type of peak parameter data to plot    
            if peak_param_type == "Microstrain" or peak_param_type == "microstrain" or peak_param_type == "Position" or peak_param_type == "position":
                microstrain = calc_strain(peak_param_time_array[start_index:end_index])*1e6
                microstrain = medfilt(microstrain, filter_data)
                peak_param_plot = microstrain
                x_label = "Microstrain"
            elif peak_param_type == "Intensity" or peak_param_type == "intensity":
                intensity = medfilt(peak_param_time_array[start_index:end_index], filter_data)
                peak_param_plot = intensity
                x_label = "Intensity"
            elif peak_param_type == "FWHM" or peak_param_type == "Fwhm" or peak_param_type == "fwhm":
                FWHM = medfilt(peak_param_time_array[start_index:end_index], filter_data)
                peak_param_plot = FWHM
                x_label = "FWHM"
            elif peak_param_type == "Relative Intensity" or peak_param_type == "relative intensity":
                relative_intensity = calc_relative_values(peak_param_time_array[start_index:end_index])
                relative_intensity = medfilt(relative_intensity, filter_data)
                peak_param_plot = relative_intensity
                x_label = "Relative Intensity"
            elif peak_param_type == "Intensity * FWHM" or peak_param_type == "intensity * fwhm":
                intensity_x_fwhm = medfilt(peak_param_time_array[start_index:end_index], filter_data)
                peak_param_plot = intensity_x_fwhm
                x_label = "Intensity * FWHM"
            elif peak_param_type == "Relative (Intensity * FWHM)" or peak_param_type == "relative (intensity * fwhm)":
                relative_intensity_x_fwhm = calc_relative_values(peak_param_time_array[start_index:end_index])
                relative_intensity_x_fwhm = medfilt(relative_intensity_x_fwhm, filter_data)
                peak_param_plot = relative_intensity_x_fwhm
                x_label = "Relative (Intensity * FWHM)"
            else:
                print(f"The peak parameter type {peak_param_type} was NOT recognised.")
                break
            ax.plot(peak_param_plot[0:number_of_points],true_stress[0:number_of_points],
                     marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
            ax.set_xlabel(x_label, fontsize=20)
            ax.set_ylabel('True Stress, ${\sigma}$, (MPa)', fontsize = 20)
            ax.minorticks_on()
            ax.legend()
            
            # label the subplots along different azimuthal angles
            if angle == 0:
                title_string = r'${0^\circ}$'
            elif angle == 90:
                title_string = r'${90^\circ}$'
            elif angle == 180:
                title_string = r'${180^\circ}$'
            elif angle == 270:
                title_string = r'${270^\circ}$'
            ax.set_title(title_string, fontsize = 20)
            
            # apply any peak parameter limits
            if peak_param_limit > 0:
                ax.set_xlim([0, peak_param_limit])
                limits_applied = True
            if peak_param_limit < 0 :
                ax.set_xlim([peak_param_limit, 0])
                limits_applied = True
            if true_stress_limit > 0:
                ax.set_ylim([0, true_stress_limit])
                limits_applied = True
            if true_stress_limit < 0 :
                ax.set_ylim([true_stress_limit, 0])
                limits_applied = True

    plt.tight_layout()
    
    # save the figures
    if limits_applied: 
        plt.savefig("{output_folder}/{x_label}_true_stress_limited_{experiment_number}.png".format(
                                                                                output_folder = output_folder,
                                                                                x_label = x_label,
                                                                                experiment_number = experiment_number),
                                                                                facecolor='white')
    elif not limits_applied:
        plt.savefig("{output_folder}/{x_label}_true_stress_{experiment_number}.png".format(
                                                                                output_folder = output_folder,
                                                                                x_label = x_label,
                                                                                experiment_number = experiment_number),
                                                                                facecolor='white')
    plt.show()
    
    # plot the peak parameter variation with applied true stress in the chosen loading direction
    print(f"Lattice {x_label} variation with applied true stress in chosen loading direction, defined at an azimuthal angle of '{azimuth_load_direction}' degrees:", end='\n\n')
    
    # create dictionary for saving lattice peak parameters
    peak_param_write = dict()
    
    # define the plot
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    
    # plot the peak parameter data for each of the lattice planes
    for peak in peak_label:
        peak_param_time_array = np.array(peak_param_time[peak][azimuth_load_direction])
        
        # choose the type of peak parameter data to plot  
        if peak_param_type == "Microstrain" or peak_param_type == "microstrain" or peak_param_type == "Position" or peak_param_type == "position":
            microstrain = calc_strain(peak_param_time_array[start_index:end_index])*1e6
            microstrain = medfilt(microstrain, filter_data)
            peak_param_plot = microstrain
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            x_label = "Microstrain"
        elif peak_param_type == "Intensity" or peak_param_type == "intensity":
            intensity = medfilt(peak_param_time_array[start_index:end_index], filter_data)
            peak_param_plot = intensity
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            x_label = "Intensity"
        elif peak_param_type == "FWHM" or peak_param_type == "Fwhm" or peak_param_type == "fwhm":
            FWHM = medfilt(peak_param_time_array[start_index:end_index], filter_data)
            peak_param_plot = FWHM
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            x_label = "FWHM"
        elif peak_param_type == "Relative Intensity" or peak_param_type == "relative intensity":
            relative_intensity = calc_relative_values(peak_param_time_array[start_index:end_index])
            relative_intensity = medfilt(relative_intensity, filter_data)
            peak_param_plot = relative_intensity
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            x_label = "Relative Intensity"
        elif peak_param_type == "Intensity * FWHM" or peak_param_type == "intensity * fwhm":
            intensity_x_fwhm = medfilt(peak_param_time_array[start_index:end_index], filter_data)
            peak_param_plot = intensity_x_fwhm
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            x_label = "Intensity * FWHM"
        elif peak_param_type == "Relative (Intensity * FWHM)" or peak_param_type == "relative (intensity * fwhm)":
            relative_intensity_x_fwhm = calc_relative_values(peak_param_time_array[start_index:end_index])
            relative_intensity_x_fwhm = medfilt(relative_intensity_x_fwhm, filter_data)
            peak_param_plot = relative_intensity_x_fwhm
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            x_label = "Relative (Intensity * FWHM)"
        plt.plot(peak_param_plot[0:number_of_points],true_stress[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        plt.legend(fontsize=20)
        plt.xlabel(x_label, fontsize = 20)
        plt.ylabel('True Stress, ${\sigma}$, (MPa)', fontsize = 20)
        plt.tight_layout()
        
        # apply any peak parameter limits
        if peak_param_limit > 0:
            plt.xlim([0, peak_param_limit])
            limits_applied = True 
        if peak_param_limit < 0 :
            plt.xlim([peak_param_limit, 0])
            limits_applied = True   
        if true_stress_limit > 0:
            plt.ylim([0, true_stress_limit])
            limits_applied = True
        if true_stress_limit < 0 :
            plt.ylim([true_stress_limit, 0])
            limits_applied = True
            
    # save the figures    
    if limits_applied:
        plt.savefig("{output_folder}/{x_label}_true_stress_load_direction_limited_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,
                                                                                 x_label = x_label,
                                                                                 experiment_number = experiment_number),
                                                                                 facecolor='white')
    elif not limits_applied:
        plt.savefig("{output_folder}/{x_label}_true_stress_load_direction_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,
                                                                                 x_label = x_label,
                                                                                 experiment_number = experiment_number),
                                                                                 facecolor='white')
    plt.show()
    
    # define the true stress for writing out
    true_stress_write = true_stress[0:number_of_points]
    
    # open a file to save the peak parameter measurements
    output_text_path =  "{output_folder}/{x_label}_true_stress_load_direction_{experiment_number}.txt".format(
                                                                             output_folder = output_folder, 
                                                                             x_label = x_label,
                                                                             experiment_number = experiment_number)
    output_text_folder = pathlib.Path(output_text_path).parent
    output_text_folder.mkdir(exist_ok=True)

    # write to the output file
    with open(output_text_path, 'w') as output_file:
        
        output_file.write(f"True Stress \t")
        
        for peak in peak_label:
            # write lattice plane peak labels at top of file
            output_file.write(f"{peak} {x_label} \t")
        
        output_file.write(f"\n")
        
        # write true stress and peak parameter values
        for i in range(len(true_stress_write)):
            output_file.write(f"{true_stress_write[i]}\t")
            for peak in peak_label:
                output_file.write(f"{peak_param_write[peak][i]}\t")
            output_file.write(f"\n")
            
    number_of_peaks = len(peak_label)        
    print(f"The lattice {x_label} variation for '{number_of_peaks}' peaks has been saved to a .txt file: '{output_text_path}'.")
    
def plot_peak_param_strain(peak_param_type: str, start_number: int, end_number: int, image_numbers: list,
                           peak_param_time: dict, true_strain: np.ndarray, 
                           peak_label: list, azimuth_load_direction: int, plane_marker: dict, plane_colour: dict, 
                           output_file_path: str, experiment_number: int, filter_data: int = 1,
                           number_of_points: int = 0, peak_param_limit: float = 0, true_strain_limit: float = 0):
    
    """ Plot a micromechanical peak parameter feature (measured from synchrotron diffraction) versus the macromechanical 
    true strain response, along different azimuthal directions, and along the loading direction. Current options for peak 
    parameter feature are Microstrain, Intensity and FWHM. Limits can be applied to constrain the plot and for consistency 
    with other plots. The plot data for the loading direction is also written to a text file.
    
    :param peak_param_type: a string defining the type of peak parameter e.g. Microstrain, Intensity, or FWHM
    :param start_number: a value defining the start point of deformation.
    :param end_number: a value defining the end point of deformation.
    :param image_numbers: a list of the diffraction pattern image numbers.
    :param peak_param_time: a dictionary of the peak parameter variation over time for different lattice plane peaks, along different directions.
    :param true_strain: an array of the true strain values already synchronised with the peak parameter variation.
    :param peak_label: a list of the lattice plane peak labels to plot.
    :param azimuth_load_direction: a value for the azimuthal angle of the loading direction.
    :param plane_marker: a dictionary of markers relating to the lattice plane peak labels.
    :param plane_colour: a dictionary of colours relating to the lattice plane peak labels.
    :param output_file_path: an output path for storing the results.
    :param experiment_number: an experiment number as reference for the test.
    :param filter_data: a value for a medium filter to smooth the synchrotron peak parameter data.
    :param number_of_points: a total number of peak parameter points to plot from the data.
    :param peak_param_limit: a peak parameter value limit for defining the maximum Y bounds of the plot.
    :param true_strain_limit: a true strain value limit for defining the maximum X bounds of the plot.
    
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
    
    # plot the peak parameter variation with applied true strain for four different orthogonal directions
    print(f"Lattice {peak_param_type} variation with applied true strain for four different orthogonal directions:")

    # define the number of subplots
    angles = [0, 90, 180, 270]
    n=2
    m=2
    fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(20,10))

    # plot the peak parameter data for each of the lattice planes
    for peak in peak_label:
        for i, ax in enumerate(axes.flatten()):
            angle = angles[i]
            peak_param_time_array = np.array(peak_param_time[peak][angle])
               
            # choose the type of peak parameter data to plot     
            if peak_param_type == "Microstrain" or peak_param_type == "microstrain" or peak_param_type == "Position" or peak_param_type == "position":
                microstrain = calc_strain(peak_param_time_array[start_index:end_index])*1e6
                microstrain = medfilt(microstrain, filter_data)
                peak_param_plot = microstrain
                y_label = "Microstrain"
            elif peak_param_type == "Intensity" or peak_param_type == "intensity":
                intensity = medfilt(peak_param_time_array[start_index:end_index], filter_data)
                peak_param_plot = intensity
                y_label = "Intensity"
            elif peak_param_type == "FWHM" or peak_param_type == "Fwhm" or peak_param_type == "fwhm":
                FWHM = medfilt(peak_param_time_array[start_index:end_index], filter_data)
                peak_param_plot = FWHM
                y_label = "FWHM"
            elif peak_param_type == "Relative Intensity" or peak_param_type == "relative intensity":
                relative_intensity = calc_relative_values(peak_param_time_array[start_index:end_index])
                relative_intensity = medfilt(relative_intensity, filter_data)
                peak_param_plot = relative_intensity
                y_label = "Relative Intensity"
            elif peak_param_type == "Intensity * FWHM" or peak_param_type == "intensity * fwhm":
                intensity_x_fwhm = medfilt(peak_param_time_array[start_index:end_index], filter_data)
                peak_param_plot = intensity_x_fwhm
                y_label = "Intensity * FWHM"
            elif peak_param_type == "Relative (Intensity * FWHM)" or peak_param_type == "relative (intensity * fwhm)":
                relative_intensity_x_fwhm = calc_relative_values(peak_param_time_array[start_index:end_index])
                relative_intensity_x_fwhm = medfilt(relative_intensity_x_fwhm, filter_data)
                peak_param_plot = relative_intensity_x_fwhm
                y_label = "Relative (Intensity * FWHM)"    
            else:
                print(f"The peak parameter type {peak_param_type} was NOT recognised.")
                break
            ax.plot(true_strain[0:number_of_points],peak_param_plot[0:number_of_points],
                    marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
            ax.set_xlabel('True Strain, ${\epsilon}$, (MPa)', fontsize = 20)
            ax.set_ylabel(y_label, fontsize=20)
            ax.minorticks_on()
            ax.legend()
            
            # label the subplots along different azimuthal angles
            if angle == 0:
                title_string = r'${0^\circ}$'
            elif angle == 90:
                title_string = r'${90^\circ}$'
            elif angle == 180:
                title_string = r'${180^\circ}$'
            elif angle == 270:
                title_string = r'${270^\circ}$'
            ax.set_title(title_string, fontsize = 20)
            
            # apply any peak parameter limits
            if true_strain_limit > 0:
                ax.set_xlim([0, true_strain_limit])
                limits_applied = True
            if true_strain_limit < 0 :
                ax.set_xlim([true_strain_limit, 0])
                limits_applied = True
            if peak_param_limit > 0:
                ax.set_ylim([0, peak_param_limit])
                limits_applied = True
            if peak_param_limit < 0 :
                ax.set_ylim([peak_param_limit, 0])
                limits_applied = True

    plt.tight_layout()
    
    # save the figures
    if limits_applied: 
        plt.savefig("{output_folder}/true_strain_{y_label}_limited_{experiment_number}.png".format(
                                                                                output_folder = output_folder,
                                                                                y_label = y_label,
                                                                                experiment_number = experiment_number),                                                                                           facecolor='white')
    elif not limits_applied:
        plt.savefig("{output_folder}/true_strain_{y_label}_{experiment_number}.png".format(
                                                                                output_folder = output_folder,
                                                                                y_label = y_label,
                                                                                experiment_number = experiment_number),
                                                                                facecolor='white') 
    plt.show()
    
    # plot the peak parameter variation with applied true strain in the chosen loading direction
    print(f"Lattice {y_label} variation with applied true strain in chosen loading direction, defined at an azimuthal angle of '{azimuth_load_direction}' degrees:", end='\n\n')
      
    # create dictionary for saving lattice peak parameters
    peak_param_write = dict()
    
    # define the plot
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    
    # plot the peak parameter data for each of the lattice planes
    for peak in peak_label: 
        peak_param_time_array = np.array(peak_param_time[peak][azimuth_load_direction])
        
        # choose the type of peak parameter data to plot 
        if peak_param_type == "Microstrain" or peak_param_type == "microstrain" or peak_param_type == "Position" or peak_param_type == "position":
            microstrain = calc_strain(peak_param_time_array[start_index:end_index])*1e6
            microstrain = medfilt(microstrain, filter_data)
            peak_param_plot = microstrain
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            y_label = "Microstrain"
        elif peak_param_type == "Intensity" or peak_param_type == "intensity":
            intensity = medfilt(peak_param_time_array[start_index:end_index], filter_data)
            peak_param_plot = intensity
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            y_label = "Intensity"
        elif peak_param_type == "FWHM" or peak_param_type == "Fwhm" or peak_param_type == "fwhm":
            FWHM = medfilt(peak_param_time_array[start_index:end_index], filter_data)
            peak_param_plot = FWHM
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            y_label = "FWHM"
        elif peak_param_type == "Relative Intensity" or peak_param_type == "relative intensity":
            relative_intensity = calc_relative_values(peak_param_time_array[start_index:end_index])
            relative_intensity = medfilt(relative_intensity, filter_data)
            peak_param_plot = relative_intensity
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            y_label = "Relative Intensity"
        elif peak_param_type == "Intensity * FWHM" or peak_param_type == "intensity * fwhm":
            intensity_x_fwhm = medfilt(peak_param_time_array[start_index:end_index], filter_data)
            peak_param_plot = intensity_x_fwhm
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            y_label = "Intensity * FWHM"
        elif peak_param_type == "Relative (Intensity * FWHM)" or peak_param_type == "relative (intensity * fwhm)":
            relative_intensity_x_fwhm = calc_relative_values(peak_param_time_array[start_index:end_index])
            relative_intensity_x_fwhm = medfilt(relative_intensity_x_fwhm, filter_data)
            peak_param_plot = relative_intensity_x_fwhm
            peak_param_write[peak] = peak_param_plot[0:number_of_points]
            y_label = "Relative (Intensity * FWHM)"
        plt.plot(true_strain[0:number_of_points], peak_param_plot[0:number_of_points],
                 marker=plane_marker[peak],color=plane_colour[peak],markersize=10,label=peak)
        plt.legend(fontsize=20)
        plt.xlabel('True Strain, ${\epsilon}$, (MPa)', fontsize = 20)
        plt.ylabel(y_label, fontsize = 20)
        plt.tight_layout()
        
        # apply any peak parameter limits
        if true_strain_limit > 0:
            plt.xlim([0, true_strain_limit])
            limits_applied = True
        if true_strain_limit < 0 :
            plt.xlim([true_strain_limit, 0])
            limits_applied = True
        if peak_param_limit > 0:
            plt.ylim([0, peak_param_limit])
            limits_applied = True
        if peak_param_limit < 0 :
            plt.ylim([peak_param_limit, 0])
            limits_applied = True
    
    # save the figures
    if limits_applied:
        plt.savefig("{output_folder}/true_strain_{y_label}_load_direction_limited_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,
                                                                                 y_label = y_label,
                                                                                 experiment_number = experiment_number),
                                                                                 facecolor='white')
    elif not limits_applied:
        plt.savefig("{output_folder}/true_strain_{y_label}_load_direction_{experiment_number}.png".format(
                                                                                 output_folder = output_folder,
                                                                                 y_label = y_label,
                                                                                 experiment_number = experiment_number),                                                                                          facecolor='white')
    plt.show()
    
    # define the true stress for writing out
    true_strain_write = true_strain[0:number_of_points]
    
    # open a file to save the peak parameter measurements
    output_text_path =  "{output_folder}/true_strain_{y_label}_load_direction_{experiment_number}.txt".format(
                                                                             output_folder = output_folder, 
                                                                             y_label = y_label,
                                                                             experiment_number = experiment_number)
    output_text_folder = pathlib.Path(output_text_path).parent
    output_text_folder.mkdir(exist_ok=True)

    # write to the output file
    with open(output_text_path, 'w') as output_file:
        
        output_file.write(f"True Strain \t")
        
        for peak in peak_label:
            # write lattice plane peak labels at top of file
            output_file.write(f"{peak} {y_label} \t")
        
        output_file.write(f"\n")
        
        # write true stress and peak parameter values
        for i in range(len(true_strain_write)):
            output_file.write(f"{true_strain_write[i]}\t")
            for peak in peak_label:
                output_file.write(f"{peak_param_write[peak][i]}\t")
            output_file.write(f"\n")
            
    number_of_peaks = len(peak_label)        
    print(f"The lattice {y_label} for '{number_of_peaks}' peaks has been saved to a .txt file: '{output_text_path}'.")