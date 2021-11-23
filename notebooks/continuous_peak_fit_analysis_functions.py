import pathlib
import re
from tqdm.notebook import tqdm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy.signal import medfilt
import yaml
from typing import Tuple
from typing import List

def get_config(path: str) -> dict:
    """Open a yaml file and return the contents."""
    with open(path) as input_file:
        return yaml.safe_load(input_file)
    
def get_image_numbers(start: int, end: int, step: int) -> List[int]:
    """Return a list of sequential image numbers given start, end and step."""
    image_numbers = list(range(start, end + 1, step))
    return image_numbers

def list_compare(a: List[str], b: List[str]):
    """Compare a list of strings and return a list of strings 
    that are do  not match."""
    set_a = set(a)  
    set_b = set(b)  
    no_match_terms = set_a.union(set_b)  - set_a.intersection(set_b)
    return no_match_terms

def extract_intensity_input(config_path: str):
    """Extract user inputs from yaml configuration file. 
    Extract input and output file paths, peak labels, data 
    resolution and image numbers. These inputs are used
    to calculate the intensity values from .fit files.
    
    :param config_path: path to the configuration file.
    
    :return: experiment number, input path for the .fit file, 
    lattice plane peak labels, data resolution, image numbers 
    - as strings, integers and a list of integers.
    """
    config = get_config(config_path)
    
    experiment_number = config["user_inputs"]["experiment_number"]
    print("The experiment number is:", experiment_number, sep='\n', end='\n\n')

    input_fit_path = config["file_paths"]["input_fit_path"]
    print("The input path to the fit file is:", input_fit_path, sep='\n', end='\n\n')
    
    peak_label = config["user_inputs"]["peak_label"]
    print("The peak labels for the peaks that are being used are:", peak_label, sep='\n', end='\n\n')

    peak_label_default = config["user_inputs"]["peak_label_default"]
    not_peaks = list_compare(peak_label, peak_label_default)
    print("The peak labels for the peaks that are NOT being used are:", not_peaks, sep='\n', end='\n\n')

    data_resolution = config["user_inputs"]["data_resolution"]
    print("The resolution of the data is:", data_resolution, "degree", end='\n\n')
    
    start = config["image_numbers"]["start"]
    end = config["image_numbers"]["end"]
    step = config["image_numbers"]["step"]
    print("The start is: ", start, "The end is ", end, "The step is ", step, sep='\n', end='\n\n')

    if config_path == "yaml/config_diamond_2021.yaml":
        # number and spacing of files
        image_numbers = np.r_[2:42+1, 45:85+1, 88:128+1, 131:171+1, 174:214+1, 217:257+1, 260:300+1, 303:343+1, 346:386+1]
    else:    
        # number and spacing of files
        image_numbers = get_image_numbers(start, end, step)
    
    return experiment_number, input_fit_path, peak_label, data_resolution, image_numbers

def extract_writing_intensity_input(config_path: str):
    """Extract user inputs from yaml configuration file. 
    Extract sample orientation plane, and output path for 
    a text file. These inputs are used to write out a text
    file containing texture intensity data in a pole figure 
    format.
    
    :param config_path: path to the configuration file.
    
    :return: plane describing sample orientation, 
    output text path for text file - as strings.
    """
    config = get_config(config_path)
    
    sample_orientation = config["user_inputs"]["sample_orientation"]
    print("The sample orientation type is:", sample_orientation, sep='\n', end='\n\n')

    plane = sample_to_plane(sample_orientation)
    print("The sample plane type is:", plane, sep='\n', end='\n\n')

    output_text_path = config["file_paths"]["output_text_path"]
    print("The output path to the text file for MTEX is:", output_text_path, sep='\n', end='\n\n')
    
    return plane, output_text_path

def extract_combine_intensity_input(config_path: str):
    """Extract user inputs from yaml configuration file. 
    Extract input and output file paths, intensity type
    and experiment numbers. These inputs are used
    to combine texture intensity data from different 
    samples (experiments)in a pole figure format.
    
    :param config_path: path to the configuration file.
    
    :return: input text path for file to combine, output text path 
    for single combined file, intensity type, experiment numbers
    to combine - as strings and a list of integers.
    """
    config_combine = get_config(config_path)
    
    input_text_path_combine = config_combine["file_paths"]["input_text_path"]
    print("The input path to the text file is:", input_text_path_combine, sep='\n', end='\n\n')

    output_text_path_combine = config_combine["file_paths"]["output_text_path"]
    print("The output path for the combined text file is:", output_text_path_combine, sep='\n', end='\n\n')

    intensity_type = config_combine["user_inputs"]["intensity_type"]
    print("The intensity type is:", intensity_type, sep='\n', end='\n\n')

    experiment_numbers_combine = config_combine["user_inputs"]["experiment_numbers"]
    print("The experiment numbers to combine are: ", experiment_numbers_combine, sep='\n', end='\n\n')
    
    start_combine = config_combine["image_numbers"]["start"]
    end_combine = config_combine["image_numbers"]["end"]
    step_combine = config_combine["image_numbers"]["step"]
    print("The start is: ", start_combine, "The end is: ", end_combine, "The step is: ", step_combine, sep='\n', end='\n\n')

    # number and spacing of files
    image_numbers_combine = get_image_numbers(start_combine, end_combine, step_combine)
    
    return input_text_path_combine, output_text_path_combine, intensity_type, experiment_numbers_combine, image_numbers_combine

def extract_powder_intensity_input(config_path: str):
    """Extract user inputs from yaml configuration file. 
    Extract input and output file paths, peak labels, data 
    resolution and image numbers. These inputs are used
    to calculate the intensity values from .fit files
    for a powder sample.
    
    :param config_path: path to the configuration file.
    
    :return: experiment number for the powder, input path for the powder .fit file, 
    lattice plane peak labels for the powder, data resolution, image numbers
    for the powder sample - as strings, integers and a list of integers.
    """
    config_powder = get_config(config_path)
    
    powder_experiment_number = config_powder["user_inputs"]["experiment_number"]
    print("The experiment number for the powder sample is:", powder_experiment_number, sep='\n', end='\n\n')

    powder_input_fit_path = config_powder["file_paths"]["input_fit_path"]
    print("The input path to the fit file for the powder sample is:", powder_input_fit_path, sep='\n', end='\n\n')

    powder_peak_label = config_powder["user_inputs"]["peak_label"]
    print("The peak labels for the powder peaks that are being used are:", powder_peak_label, sep='\n', end='\n\n')

    powder_peak_label_default = config_powder["user_inputs"]["peak_label_default"]
    powder_not_peaks = list_compare(powder_peak_label, powder_peak_label_default)
    print("The peak labels for the powder peaks that are NOT being used are:", powder_not_peaks, sep='\n', end='\n\n')
    
    powder_data_resolution = config_powder["user_inputs"]["data_resolution"]
    print("The resolution of the powder data is:", powder_data_resolution, "degree", end='\n\n')
    
    powder_start = config_powder["image_numbers"]["start"]
    powder_end = config_powder["image_numbers"]["end"]
    powder_step = config_powder["image_numbers"]["step"]
    print("The start is: ", powder_start, "The end is: ", powder_end, "The step is: ", powder_step, sep='\n', end='\n\n')

    # number and spacing of files
    powder_image_numbers = get_image_numbers(powder_start, powder_end, powder_step)
    
    return powder_experiment_number, powder_input_fit_path, powder_peak_label, powder_data_resolution, powder_image_numbers

def read_fit_results (experiment_number: int, input_fit_path: str, peak_label: list, 
                      data_resolution:int, image_numbers = List[int]):
    """This function loops through refined '.fit' files produced using
    the python package Continuous-Peak-Fit and searches for the peak position, 
    intensity, half-width and Pseudo-Voigt weighting results. 
    
    :param experiment_number: input experiment number.
    :param input_fit_path: input path to the .fit file containing the results.
    :param peak_label: lattice plane peak labels.
    :param data_resolution: azimuthal resolution of intensity data, in degrees.
    :param image_numbers: a list of diffraction pattern image numbers.
    
    :return: peak position, peak intensity, peak half-width and peak Pseudo-Voigt weighted fraction
    as nested dictionaries.
    """
    # define dictionaries to save results to
    peak_position = dict()
    peak_intensity = dict()
    peak_halfwidth = dict()
    peak_PV_weight = dict()
    
    for image_number in tqdm(image_numbers):
        input_fit_file = input_fit_path.format(experiment_number=experiment_number, image_number=image_number)
        
        # dictionary to save results to
        peak_position[image_number] = dict()
        peak_intensity[image_number] = dict()
        peak_halfwidth[image_number] = dict()
        peak_PV_weight[image_number] = dict()
        
        with open(input_fit_file, 'r') as results_file:  
            line = results_file.readline()
            peak_number = 0
            
            while line:
                if '# peak number' in line:
                    peak_position[image_number][peak_label[peak_number]]=[]
                    peak_intensity[image_number][peak_label[peak_number]]=[]
                    peak_halfwidth[image_number][peak_label[peak_number]]=[]
                    peak_PV_weight[image_number][peak_label[peak_number]]=[]

                    for azimuth_degree in range (0, 360, data_resolution):
                        line = results_file.readline()
                        fit_result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                        peak_position[image_number][peak_label[peak_number]].append(float(fit_result[0]))
                        peak_intensity[image_number][peak_label[peak_number]].append(float(fit_result[1]))
                        peak_halfwidth[image_number][peak_label[peak_number]].append(float(fit_result[2]))
                        peak_PV_weight[image_number][peak_label[peak_number]].append(float(fit_result[3]))

                    peak_number+=1

                else:
                    line = results_file.readline()

    return peak_position, peak_intensity, peak_halfwidth, peak_PV_weight

def sample_to_plane(sample_orientation: str):
    """Return a Cartesian circle plane type for a given sample orienation type"""
    sample_to_plane = {'S1': 'YZ', 'S2': 'XZ', 'S3': 'XY', 'S4': 'YX to YZ', 'S5': 'XY to XZ', 'S6': 'XZ to YZ'}
    plane = sample_to_plane[sample_orientation]
    return plane

def intensity_to_texture_file(experiment_number: int, intensity_type: str, output_text_path: str, peak_intensity: dict, 
                              peak_label: list, plane: str, data_resolution: int, image_numbers: List[int]):
    """This function calculates the corresponding spherical polar coordinates
    (polar and azimuthal angles) for the set of intensity values and 
    writes out a text file of the data that can be read in MTEX.
    
    :param experiment_number: input experiment number.
    :param intensity_type: the type of intensity, either 'raw' or 'powder-calibrated'
    :param output_text_path: output path to save the intensity results.
    :param peak_intensity: diffraction ring intensities from different lattice planes.
    :param peak_label: lattice plane peak labels.
    :param plane: setting lattice plane orientation, 'YZ', 'XZ', 'XY', 'YX to YZ', 'XY to XZ', 'XZ to YZ'.
    :param data_resolution: azimuthal resolution of intensities in degrees, usually set as 1 degree.
    :param image_numbers: a list of diffraction pattern image numbers.
    
    """
    count = 0
    
    for image_number in tqdm(image_numbers):
    
        for label in peak_label:
            output_path =  output_text_path.format(experiment_number=experiment_number, intensity_type=intensity_type, image_number=image_number, label=label)
            output_folder = pathlib.Path(output_path).parent
            output_folder.mkdir(exist_ok=True)

            with open(output_path, 'w') as output_file:

                # write metadata for the top of the file
                output_file.write('Polar Angle \t Azimuth Angle \t Intensity \n')

                # iterate through the peak intensities
                for i in range(0, len(peak_intensity[image_number][label])):

                    # set the angle around the circle (diffraction pattern ring) from horizontal position
                    alpha = i*data_resolution

                    # set the inclination of any inclined planes to 45 degrees
                    beta = (np.pi)/4

                    # use the circle parametrisation formula to calculate x,y,z values
                    if plane == 'XY':
                        x = np.cos(np.deg2rad(alpha))
                        y = np.sin(np.deg2rad(alpha))
                        z = 0

                    if plane == 'XZ':
                        x = np.cos(np.deg2rad(alpha))
                        y = 0
                        z = np.sin(np.deg2rad(alpha))

                    if plane == 'YZ':
                        x = 0
                        y = np.cos(np.deg2rad(alpha))
                        z = np.sin(np.deg2rad(alpha))

                    if plane == 'XY to XZ':
                        x = np.cos(np.deg2rad(alpha))
                        y = np.sin(np.deg2rad(alpha))*np.cos(beta)
                        z = np.sin(np.deg2rad(alpha))*np.sin(beta)

                    if plane == 'YX to YZ':
                        x = np.sin(np.deg2rad(alpha))*np.cos(beta)
                        y = np.cos(np.deg2rad(alpha))
                        z = np.sin(np.deg2rad(alpha))*np.sin(beta)

                    if plane == 'XZ to YZ':
                        x = np.cos(np.deg2rad(alpha))*np.cos(beta)
                        y = np.cos(np.deg2rad(alpha))*np.sin(beta)
                        z = np.sin(np.deg2rad(alpha))

                    # calulate the spherical polar coordinates from cartesian coordinates using the standard equations
                    theta = np.rad2deg(np.arccos(z))
                    # arctan2 needed to handle negative values for phi values
                    phi = np.rad2deg(np.arctan2(y,x))
                    # convert phi scale from -180, 180 to 0, 360
                    if phi < 0:
                        phi = phi + 360

                    output_file.write(f'{theta}\t'
                                      f'{phi}\t'
                                      f'{peak_intensity[image_number][label][i]}\n')
        count+=1
        
    print(f"Written '{count}' set of {intensity_type} intensity .txt data files to: '{output_path}'.")
            
def combine_texture_files (input_text_path: str, output_text_path: str, intensity_type: str, 
                           peak_label: list, experiment_numbers: List[int], image_numbers: List[int]):
    """This function combines the intensity and spherical polar coordinates of
    multiple files into one file, by writing the data sequentially to a new 
    text file.
    
    :param input_text_path: path to the text files containing intensity and polar coordinates.
    :param output_text_path: output path to save the combined intensity results.
    :param intensity_type: name for input and output path of text file, either 'raw' or 'powder-corrected'.
    :param peak_label: lattice plane peak labels.
    :param experiment_numbers: list of experiment numbers of files to combine.
    
    """
    
    experiment_start = experiment_numbers[0]
    experiment_end = experiment_numbers[-1]

    for image_number in image_numbers:
    
        for label in tqdm(peak_label):
            output_path = output_text_path.format(experiment_start=experiment_start, experiment_end=experiment_end, intensity_type=intensity_type, image_number=image_number, label=label)
            output_folder = pathlib.Path(output_path).parent
            output_folder.mkdir(exist_ok=True)
            # overwrite any existing output file

            with open(output_path, 'w') as output_file:
                # write metadata for the top of the file
                output_file.write('Polar Angle \t Azimuth Angle \t Intensity \n')

            for experiment_number in experiment_numbers:
                input_path = input_text_path.format(experiment_number=experiment_number, intensity_type=intensity_type, image_number=image_number, label=label)

                # open output file in append mode to add lines
                with open(output_path, 'a') as output_file:

                    with open(input_path, 'r') as results_file:  
                        line = results_file.readline()
                        line = results_file.readline()

                        while line:
                            output_file.write(line)
                            line = results_file.readline()

            print(f"Written {intensity_type} intensity data for '...{input_path[-24:]}' to: '...{output_path[-35:]}'.")
        
def calibrate_intensity_to_powder(peak_intensity: dict, powder_peak_intensity: dict,
                                  powder_peak_label: List[str], image_numbers: List[int], powder_start: int = 1):
    """Calibrate peak intensity values to intensity measurements taken from a 'random' powder sample."""
    corrected_peak_intensity = dict()
    first_iteration = True

    for image_number in tqdm(image_numbers):
        corrected_peak_intensity[image_number] = dict()

        for label in powder_peak_label:
            powder_average = np.average(powder_peak_intensity[powder_start][label])
            powder_error = np.std(powder_peak_intensity[powder_start][label], ddof=1)

            corrected_peak_intensity[image_number][label] = []                            
            corrected_peak_intensity[image_number][label] = peak_intensity[image_number][label] / powder_average

            if first_iteration:
                print(f"Normalised {label} intensities by a value of {powder_average} +/- {powder_error} from average powder intensity.")
            else:
                continue
     
        first_iteration = False
            
    return corrected_peak_intensity