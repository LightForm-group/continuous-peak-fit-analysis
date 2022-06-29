import pathlib
import re
import os
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

def extract_analysis_input(config_path: str):
    """Extract user inputs from yaml configuration file. 
    Extract input and output file paths, peak labels, data 
    resolution and image numbers. These inputs are used
    to calculate the single peak fit values from .fit files.
    
    :param config_path: path to the configuration file.
    
    :return: experiment number, input path for the .fit file, 
    lattice plane peak labels, data resolution, image numbers,
    - as strings, integers and a list of integers.
    """
    
    experiment_number, input_fit_path, peak_label, data_resolution, image_numbers, image_numbers_sorted = analysis.extract_intensity_input(config_path)

    return experiment_number, input_fit_path, peak_label, data_resolution, image_numbers, image_numbers_sorted

def extract_thermomechanical_input(config_path: str):
    """ Extract user inputs for deformation equipment,
    (including deformation start and end numbers), as well 
    as input and output file paths, peak labels, data 
    resolution and image numbers. These inputs are used
    to calculate the intensity values from .fit files.
    
    :param config_path: path to the configuration file.
    
    :return: the path for the thermomechanical data during deformation, 
    the start and end of deformation, the number of frames, the acquisition 
    frequency of SXRD images and deformation data, the output file path, 
    and if it is needed the file path for data recorded from the analogue 
    output, including conversions for load, temperature and position.
    - as strings, integers and a list of integers.
    """
    config = analysis.get_config(config_path)
    
    thermomechanical_equipment = config["deformation_input"]["thermomechanical_equipment"]
    print("The thermomechanical equipment used for the experiment is:", thermomechanical_equipment, sep='\n', end='\n\n')
    
    thermomechanical_file_path = config["deformation_input"]["thermomechanical_file_path"]
    print("The input path for the thermomechanical data is:", thermomechanical_file_path, sep='\n', end='\n\n')
    
    start_deformation = config["deformation_input"]["start_deformation"]
    end_deformation = config["deformation_input"]["end_deformation"]
    
    if start_deformation and end_deformation:
        print("The start of deformation is number:", start_deformation, sep='\n', end='\n\n')
        print("The end of deformation is number:", end_deformation, sep='\n', end='\n\n')
        number_of_frames = int(end_deformation - start_deformation)
        print("The number of frames has been calculated as:", number_of_frames, sep='\n', end='\n\n')
    
    else:
        print("Using only INITIAL guesses for start and end deformation, please correct these values later.", end='\n\n')
        start_deformation = config["deformation_input"]["start_deformation_initial"]
        end_deformation = config["deformation_input"]["end_deformation_initial"]
        print("The initial guess for start of deformation is number:", start_deformation, sep='\n', end='\n\n')
        print("The initial guess for end of deformation is number:", end_deformation, sep='\n', end='\n\n')
        number_of_frames = int((end_deformation - start_deformation) / 4)
        print("The number of frames has been calculated as:", number_of_frames, sep='\n', end='\n\n')
    
    acquisition_frequency_sxrd = config["deformation_input"]["acquisition_frequency_sxrd"]
    print("The acquisition frequency of the SXRD pattern images during deformation (in Hz) is:", acquisition_frequency_sxrd, sep='\n', end='\n\n')
    
    minimum_stress = config["deformation_input"]["minimum_stress"]
    print("The minimum stress to detect the start of deformation (in MPa) is:", minimum_stress, sep='\n', end='\n\n')
    
    deform_sequence = config["deformation_input"]["deform_sequence"]
    print("The sequence length to detect the start of deformation is:", deform_sequence, sep='\n', end='\n\n')
    
    filter_equipment = config["deformation_input"]["filter_equipment"]
    print("A median filter is being applied to the equipment data, with a value of:", filter_equipment, sep='\n', end='\n\n')
    
    output_file_path = config["deformation_input"]["output_file_path"]
    print("The output file path for saving the plots in the notebook is:", output_file_path, sep='\n', end='\n\n')
        
    return thermomechanical_equipment, thermomechanical_file_path, start_deformation, end_deformation, number_of_frames, acquisition_frequency_sxrd, minimum_stress, deform_sequence, filter_equipment, output_file_path

def extract_analogue_input(config_path:str):
    """ Extract user inputs for deformation equipment,
    (including deformation start and end numbers), as well 
    as input and output file paths, peak labels, data 
    resolution and image numbers. These inputs are used
    to calculate the intensity values from .fit files.
    
    :param config_path: path to the configuration file.
    
    :return: the path for the thermomechanical data during deformation, 
    the start and end of deformation, the number of frames, the acquisition 
    frequency of SXRD images and deformation data, the output file path, 
    and if it is needed the file path for data recorded from the analogue 
    output, including conversions for load, temperature and position.
    - as strings, integers and a list of integers.
    """
    config = analysis.get_config(config_path)
    
    analogue_data_file_path = config["deformation_input"]["analogue_data_file_path"]
    
    if analogue_data_file_path:

        print("Thermomechanical analogue output HAS been provided - use OPTION 2 (synchronised thermomechanical analogue output) to synchronise data.", end='\n\n')

        print("The input file path for the thermomechanical analogue output, used to correlate the diffraction pattern images with the deformation conditions, is:", analogue_data_file_path, sep='\n', end='\n\n')

        load_conversion = config["deformation_input"]["load_conversion"]
        print("The analogue load conversion (Newtons/Volt) is:", load_conversion, sep='\n', end='\n\n')

        temperature_conversion = config["deformation_input"]["temperature_conversion"]
        print("The analogue temperature conversion (Celsius/Volt) is:", temperature_conversion, sep='\n', end='\n\n')

        position_conversion = config["deformation_input"]["position_conversion"]
        print("The analogue position conversion (Millimetre/Volt) is:", position_conversion, sep='\n', end='\n\n')

    elif not analogue_data_file_path:

        print("Thermomechanical analogue output has NOT been provided - use OPTION 1 (lattice microstrain) to synchronise data.", end='\n\n')

        load_conversion = False
        temperature_conversion = False
        position_conversion = False
        
    return analogue_data_file_path, load_conversion, temperature_conversion, position_conversion
    
def restructure_fit_results(image_numbers: list, peak_label: list, data_resolution: int,
                            peak_position: dict, peak_intensity: dict, peak_halfwidth: dict, peak_PV_weight: dict):
    """This function returns the single peak data of specific lattice planes,
    at specific azimuthal angles, over time. The peak data is captured from the nested 
    dictionaries containing the peak position, intensity, half-width and Pseudo-Voigt 
    weighting results and written to new 'restructured' dictionaries. Restructuring the
    data in this way makes it easier to analyse the changes caused by deformation, over time.
     
    :param image_numbers: a list of diffraction pattern image numbers.
    :peak_label: list of lattice plane labels.
    :peak_position: dictionary of the peak positions for all peaks, at all azimuthal angles, for different files.
    :peak_intensity: dictionary of the peak intensities for all peaks, at all azimuthal angles, for different files.
    :peak_halfwidth: dictionary of the peak half-widths for all peaks, at all azimuthal angles, for different files.
    :peak_PV_weight: dictionary of the peak Pseudo-Voigt weighted fractions for all peaks, at all azimuthal angles, 
                     for different files.
    
    :return: peak position, peak intensity, peak half-width and peak Pseudo-Voigt weighted fraction
    as nested dictionaries.
    """
    
    # create list of peak numbers as they are labelled in the .fit file, starting at 1
    peak_numbers = list(range(1, len(peak_label)+1))
    
    # create list of azimuthal degree as in the .fit file, starting at 0
    azimuth_degree = list(range(0, 360, data_resolution))
    
    peak_position_time = dict()
    peak_intensity_time = dict()
    peak_halfwidth_time = dict()
    peak_PV_weight_time = dict()
        
    for number, label in zip(peak_numbers, peak_label):
        peak_position_time[label] = dict()
        peak_intensity_time[label] = dict()
        peak_halfwidth_time[label] = dict()
        peak_PV_weight_time[label] = dict()
        
        for azimuth in azimuth_degree:
            peak_position_time[label][azimuth] = []
            peak_intensity_time[label][azimuth] = []
            peak_halfwidth_time[label][azimuth] = []
            peak_PV_weight_time[label][azimuth] = []

            # iterate through different blocks of image numbers
            for i in range(len(image_numbers)):
                for image_number in image_numbers[i]:
                    peak_position_time[label][azimuth].append(peak_position[image_number][label][azimuth])
                    peak_intensity_time[label][azimuth].append(peak_intensity[image_number][label][azimuth])
                    peak_halfwidth_time[label][azimuth].append(peak_halfwidth[image_number][label][azimuth])
                    peak_PV_weight_time[label][azimuth].append(peak_PV_weight[image_number][label][azimuth])
                    
    return(peak_position_time, peak_intensity_time, peak_halfwidth_time, peak_PV_weight_time)

def sequence_checker(array, sequence_length: int = 4):
    """ Check for sequence of consecutive numbers in array
    and return array when sequence has been found.
    """
    new_array = []
    for i in range(len(array) - 1):
        # array[i] + 1 is for checking equivalence of consecutive numbers
        if(array[i] + 1 == array[i + 1]):
            new_array += [array[i]]
            if(len(new_array) == sequence_length):
                break
        else:
            new_array = []
    return new_array

def closest_value (number, array):
    value = array[0]
    for index in range (len(array)):
        if abs (number - array[index]) < abs (number - value):
            value = array[index]
            element = index
    return value, element

def match_array_numbers(image_numbers, start_number, end_number):

    start_value, start_index = closest_value(start_number, image_numbers)
    end_value, end_index = closest_value(end_number, image_numbers)

    print("The start image number is ", start_value, ", which is the", start_index, "index in the image number list.", end='\n\n')
    print("The end image number is ", end_value, ", which is the", end_index, "index in the image number list.", end='\n\n')
    
    return start_value, start_index, end_value, end_index

def load_ETMT_data(etmt_file_path):
    
    print("Loading ETMT data.", end='\n\n')
          
    etmt_data = np.loadtxt(etmt_file_path, delimiter=',', skiprows=1)
    
    time = etmt_data[:,0]
    force = etmt_data[:,1]
    position = etmt_data[:,2]
    stress = etmt_data[:,3]
    true_strain = etmt_data[:,4]
    true_stress = etmt_data[:,5]
    temperature_etmt = etmt_data[:,6]
    temperature_eurotherm = etmt_data[:,7]
    frame_signal = etmt_data[:,8]
    
    return time, force, position, stress, true_strain, true_stress, temperature_etmt, temperature_eurotherm, frame_signal
    
def load_dilatometer_data(dilatometer_file_path):
    
    print("Loading Dilatometer data.", end='\n\n')

    dilatometer_file = open(dilatometer_file_path,'r',encoding='latin-1')
    dilatometer_data = np.loadtxt(dilatometer_file, skiprows=3)
    
    points = dilatometer_data[:,0]
    time = dilatometer_data[:,1]
    temperature = dilatometer_data[:,2]
    delta_length = dilatometer_data[:,3]
    force = dilatometer_data[:,4]
    strain = dilatometer_data[:,5]
    true_stress = dilatometer_data[:,6]
    true_strain = dilatometer_data[:,7]
    true_strain_rate = dilatometer_data[:,8]
    
    return points, time, temperature, delta_length, force, strain, true_stress, true_strain, true_strain_rate

def load_analogue_data(analogue_file_path, load_conversion, temp_conversion, position_conversion):
    
    print("Loading analogue data, which is synchronised with the synchrotron acquisition frequency.", sep='\n', end='\n\n')
    
    analogue_data = np.loadtxt(analogue_file_path, skiprows=6)
    max_frame = len(analogue_data)
   
    frame_numbers = analogue_data[:,1]
    load = analogue_data[:,1] * load_conversion
    temperature = analogue_data[:,2] * temp_conversion
    position = analogue_data[:,3] * position_conversion
    
    print("Note, the maximum diffraction pattern image number recorded was :", max_frame)
    
    return frame_numbers, load, temperature, position, max_frame

def plot_thermomechanical_data(thermomech_equipment: str, thermomech_file_path: str, output_file_path: str, 
                               experiment_number: int, minimum_stress: int = 1, deform_sequence: int = 4, 
                               number_deform_frames: int = 1000, acquisition_frequency_sxrd: int = 10,  
                               filter_data: int = 1):
    """ Plot true stress, true stress versus true strain, and true stress versus true strain 
    at the frequency of SXRD images from data recorded from the ETMT or Dilatometer.
    
    :param file_path_etmt_data: input file path string.
    :param first_point: value defining the start point of deformation.
    :param last_point: value defining the end point of deformation.
    :param acquisition_freq_sxrd: acquisition frequency of the SXRD detector in Hz (default is 10 Hz).
    :param acquisition_freq_etmt: cacquisition frequency of the ETMT data recorder in Hz (default is 50 Hz).
    :param filter_data: size of the median filter window to filter the data with medfilt function (default is ).
    
    :return: NumPy arrays for the true stress and true strain.
    """
    # load the thermomechanical data
        
    if thermomech_equipment == "ETMT":
        # at low strain applied stress is approximately true stress, so can use applied stress directly here
        time, force, position, true_stress, true_strain, truer_stress, temperature_etmt, temperature_eurotherm, frame_signal = load_ETMT_data(thermomech_file_path)
        print("Warning! Using Applied Stress as True Stress. Only valid for low strains. Alter script [here] to use True Stress from Resistance Method.", end='\n\n')
        
    elif thermomech_equipment == "Dilatometer":
        points, time, temperature, delta_length, force, \
        strain, true_stress, true_strain, true_strain_rate = load_dilatometer_data(thermomech_file_path)
        
    else:
        print("Thermomechanical equipment not recognised, expected either ETMT or Dilatometer", end='\n\n')
        return
    
    # calculate the acquisition frequency of the thermomechanical data and ratio to the SXRD pattern images
    acquisition_frequency_thermomech = 1 / np.average(np.diff(time))
    print(f"The acquisition frequency of the {thermomech_equipment} data is:", acquisition_frequency_thermomech, " Hz", end='\n\n')

    acquisition_frequency_ratio = float(acquisition_frequency_thermomech / acquisition_frequency_sxrd)
    print(f"The ratio of {thermomech_equipment}-to-SXRD acquisition is:", acquisition_frequency_ratio, end='\n\n')
    
    deform_end = int(acquisition_frequency_ratio * number_deform_frames)

    if thermomech_equipment == "ETMT":
        deforming = np.where(true_stress > minimum_stress)
        deform_start = deforming[0][0]
        print("The deformation begins at array index:", deform_start, end='\n\n')
    
    elif thermomech_equipment == "Dilatometer":
        # find the start of deformation - define as sequence of ? points with stress greater than ? MPa
        deforming = np.where(true_stress > minimum_stress)
        deforming_sequence = sequence_checker(deforming[0], deform_sequence)
        deform_start = deforming_sequence[0]
        print("The deformation begins at array index:", deform_start, end='\n\n')
    
    # define the end of deformation
    print("Deform Frames: ", len(true_stress))
    deform_end = int(deform_start + (acquisition_frequency_ratio * number_deform_frames))
    print("The deformation ends at array index:", deform_end, end='\n\n')
    
    # the strain may need shifting a little if it does not start at zero during deformation
    strain_shift = np.average(true_strain[0:deform_start])
    true_strain = true_strain + math.sqrt(strain_shift * strain_shift)
    print("The strain has been shifted by an amount:", math.sqrt(strain_shift * strain_shift), " to start at zero", end='\n\n')

    # some filtering of the data is needed due to fluctuations in the thermomechanical data
    filter_strain = medfilt(true_strain[deform_start:deform_end],filter_data)
    filter_stress = medfilt(true_stress[deform_start:deform_end],filter_data)
    
    # plot the true stress for each point in the thermomechanical data
    print(f"{thermomech_equipment} unfiltered true stress versus data number:")
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    plt.plot(true_stress,'-o', color='blue',markersize=10)
#     plt.title(f'{thermomech_equipment} Data', fontsize = 20)
    plt.ylabel('True Stress, ${\sigma}$ (MPa)', fontsize = 20)
    plt.xlabel('Data Number', fontsize = 20)
    plt.show()
    
    # plot the true stress versus true strain at the thermomechanical acquisition frequency
    print(f"{thermomech_equipment} true stress-strain at thermomechanical acquisition frequency:")
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    plt.plot(filter_strain,filter_stress,'-o',color='blue', markersize=10)
#     plt.title(f'{thermomech_equipment} Data', fontsize = 20)
    plt.ylabel('True Stress, ${\sigma}$ (MPa)', fontsize = 20)
    plt.xlabel('True Strain, ${\epsilon}$', fontsize = 20)
    plt.show()
    
    # plot the true stress versus true strain, with each point representing a diffraction pattern image
    print(f"{thermomech_equipment} true stress-strain at SXRD frequency:")
    true_strain = np.zeros([number_deform_frames,])
    true_stress = np.zeros([number_deform_frames,])
    for image in range(0, number_deform_frames):
        true_strain[image] = filter_strain[int(image*acquisition_frequency_ratio)]
        true_stress[image] = filter_stress[int(image*acquisition_frequency_ratio)]  
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    plt.plot(true_strain, true_stress, 'o',color='blue', markersize=10)
#     plt.title(f'{thermomech_equipment} Data at SXRD Frequency', fontsize = 20)
    plt.ylabel('True Stress, $\sigma$ (MPa)', fontsize = 20)
    plt.xlabel('True Strain, $\epsilon$', fontsize = 20)
    plt.tight_layout()
    
    output_folder = output_file_path.format(experiment_number = experiment_number)
    
    # check output folder exists
    CHECK_FOLDER = os.path.isdir(output_folder)

    if not CHECK_FOLDER:
        os.makedirs(output_folder)
        print("Created folder : ", output_folder)

    plt.savefig("{output_folder}/true_stress_strain_{experiment_number}.png".format(output_folder = output_folder,  
                                                                                    experiment_number = experiment_number))
    plt.show()
    
    return (true_stress, true_strain)

def plot_analogue_data(analogue_file_path: str, start_number: int, end_number: int, 
                       load_conversion: int = 25, temp_conversion: int = 150, position_conversion = 0.5): 
    
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
    
    # load the analogue data
    frame_numbers, load, temperature, position, max_frame = load_analogue_data(analogue_file_path, load_conversion, temp_conversion, position_conversion)
    
    # match the start and end numbers to values and indices in the arrays
    start_value, start_index, end_value, end_index = match_array_numbers(frame_numbers, start_number, end_number)
    
    print("Adjust the start and end image number values until you only capture the deforming region, with a charateristic change in the measured load response.", end='\n\n')
        
    # use the start and end indices to plot microstrain versus frame number
    print("Analogue temperaure measurements for the entire experiment:")
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    plt.plot(frame_numbers,temperature,color='blue')
    plt.legend(fontsize = 20)
    plt.xlabel("Frame Number", fontsize = 20)
    plt.ylabel(r"Temperature ${(^\circ C)}$", fontsize = 20)    
    plt.show()

    print("Analogue position measurements for the entire experiment:")    
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    plt.plot(frame_numbers,position,color='blue')
    plt.legend(fontsize = 20)
    plt.xlabel("Frame Number", fontsize = 20)
    plt.ylabel("Gauge Position (mm)", fontsize = 20)    
    plt.show()

    print("Analogue load measurements, reduced to capture just the deforming region:")
    plt.figure(figsize=(10,8))
    plt.minorticks_on()
    plt.plot(frame_numbers[start_index:end_index],load[start_index:end_index],color='blue')
    plt.legend(fontsize = 20)
    plt.xlabel("Frame Number", fontsize = 20)
    plt.ylabel("Load (N)", fontsize = 20)    
    plt.show()