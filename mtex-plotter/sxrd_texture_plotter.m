%% SXRD_TEXTURE_PLOTTER
% This script can be used  for the batch processing of synchrotron
% intensity data, written in spherical polar coordinate format.
% The script can be used for texture calculation, plotting of pole figures, 
% plotting of ODFs and calculation of texture strength values. 
% It can currentlysss be used for both alpha and beta phases in titanium alloys.
% But, it could easily be adapted for any phase in a crystal material...

%% Define the user input configuration file

% Define the user input configuration file here...
% Note, this should be the only line you need to change in this script.
% Then you will be asked to select an input folder, containing  the
% intensity data files, and then asked to select an output folder, to save
% the ODFs, PFs and a text file containing the texture strength values.

%user_inputs_filepath = 'json/diamond/config_diamond_2022_additional_stage_scan_beta.json'
%user_inputs_filepath = 'json/diamond/config_diamond_2022_beta_027.json'
user_inputs_filepath = 'json/diamond/config_diamond_2021_summed_alpha.json'
%user_inputs_filepath = 'json/diamond/config_diamond_2017_beta.json'
%user_inputs_filepath = 'json/desy/config_desy_2020_alpha_09b_volume_fraction.json'

% defining ODF for modelling
%user_inputs_filepath = 'json/diamond/config_diamond_2022_alpha_034.json'

%% Load user inputs from JSON file

% load the user inputs from JSON file
user_inputs = loadjson(user_inputs_filepath)

% specify the experiment number
experiment_number = user_inputs.experiment_number.value
experiment_number_characters = user_inputs.experiment_number.characters

% specify the data type, eg. individual, summed, or combined
data_type = user_inputs.data_type

% specify the test numbers
test_number_characters = user_inputs.test_number.characters

% specify the number of stages - important for multi stage experiments containing non consecutive arrays
test_number_fields = fields(user_inputs.test_number);
number_of_stages = length(test_number_fields) - 1

for i = 1:number_of_stages
    
    % read in the test number array for each stage
    stage = test_number_fields{i+1}
    test_number_start = user_inputs.test_number.(stage).start
    test_number_end = user_inputs.test_number.(stage).end
    test_number_step = user_inputs.test_number.(stage).step
    
    % specify the length of the test number array, specifying a block of consecutive numbers
    test_number_length = length(test_number_start);
    
    % initialise array to store the test numbers
    test_number.(stage) = [];
    
    for j = 1:test_number_length
        % calculate the block of consecutive numbers and append to an array of test numbers for each stage
        test_number_section = test_number_start(j):test_number_step(j):test_number_end(j);
        test_number.(stage) = [test_number.(stage), test_number_section];
    end
end

% specify the phase
phase = user_inputs.phase

% specify the plotting convention
xAxisDirection = user_inputs.plotting_convention.xAxisDirection
zAxisDirection = user_inputs.plotting_convention.zAxisDirection
setMTEXpref('xAxisDirection',xAxisDirection)
setMTEXpref('zAxisDirection',zAxisDirection)

% specify any rotation to the data (not usually required)
euler1 = user_inputs.rotation.euler1
euler2 = user_inputs.rotation.euler2
euler3 = user_inputs.rotation.euler3

% set the pole figure maxima
pf_max = user_inputs.pole_figure_params.pf_max
pf_contour_step = user_inputs.pole_figure_params.contour_step

% specify the ODF resolution
odf_resolution = user_inputs.odf_params.odf_resolution
odf_resolution = odf_resolution*degree
odf_max = user_inputs.odf_params.odf_max
odf_misorientation = user_inputs.odf_params.odf_misorientation

%% Select Input and Output Directories

for i = 1:number_of_stages
    stage = test_number_fields{i+1}
    
    disp('Please navigate to the input directory, where the texture intensity data files are stored.');
    inputDir.(stage) = uigetdir; % gets input directory

    disp('Please navigate to the output directory, where you would like to save the texture results.');
    outputDir.(stage) = uigetdir; % gets output directory
end

%% Specify Format

% define experiment number as a string

if experiment_number_characters == 2
    experiment_format_spec = '%02.f';
    experiment_number_string = num2str(experiment_number, experiment_format_spec)

elseif experiment_number_characters == 3
    experiment_format_spec = '%03.f';
    experiment_number_string = num2str(experiment_number, experiment_format_spec)

elseif experiment_number_characters == 6
    experiment_format_spec = '%06.f';
    experiment_number_string = num2str(experiment_number, experiment_format_spec)
    
 else
    disp('Number of characters for experiment number not recognised.');
    return;
end

% define test number as string

if test_number_characters == 1
    testFormat = '%01.f';
    
elseif test_number_characters == 2
    testFormat = '%02.f';

elseif test_number_characters == 3
    testFormat = '%03.f';
    
elseif test_number_characters == 4
    testFormat = '%04.f';

elseif test_number_characters == 5
    testFormat = '%05.f';
    
else
    disp('Number of characters for test number not recognised.');
    return;
end

%% Analyse Intensity Data

odf_return = 'no'

for i = 1:number_of_stages
    
    % define output path open file to save the texture values
    stage = test_number_fields{i+1}
    output_text_file = fopen(fullfile(outputDir.(stage), strcat(experiment_number_string,'_texture_strength.txt')),'w')
    
    if strcmp(phase, 'alpha')
        % print header for alpha phase texture measurements
        fprintf(output_text_file, 'Test Number \t Texture Index \t ODF Max \t phi1 Angle of ODF Max \t PHI Angle of ODF Max \t phi2 Angle of ODF Max \t {0002} PF Max \t {10-10} PF Max \t {11-20} PF Max \t Basal TD Volume Fraction \t Basal ND Volume Fraction \t Basal RD Volume Fraction \t Basal 45 Volume Fraction \t Reconstruction RP Error \n');

        % define alpha crystal symmetry
        CS = crystalSymmetry('6/mmm', [2.954 2.954 4.729], 'X||b*', 'Y||a', 'Z||c*', 'mineral', 'Titanium Alpha', 'color', 'light blue');
        
        % analyse, plot and save alpha texture
        [TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
        PF_basal_max, PF_prismatic1_max, PF_prismatic2_max, odf] = alpha_texture_plotter(user_inputs_filepath, inputDir.(stage), data_type,... 
                                                                                                phase, experiment_number_string, test_number.(stage), testFormat,... 
                                                                                                outputDir.(stage), output_text_file,....
                                                                                                CS, odf_max, odf_resolution, odf_misorientation,...
                                                                                                euler1, euler2, euler3,...
                                                                                                pf_max, pf_contour_step,...
                                                                                                odf_return)      
    elseif strcmp(phase, 'beta')
        % print header for beta phase texture measurements
        fprintf(output_text_file, 'Test Number \t Texture Index \t ODF Max \t phi1 Angle of ODF Max \t PHI Angle of ODF Max \t phi2 Angle of ODF Max \t {001} PF Max \t {110} PF Max \t {111} PF Max \t Cube Volume Fraction \t Rotated Cube Volume Fraction \t Alpha Fibre Volume Fraction \t Gamma Fibre Volume Fraction \t Reconstruction RP Error \n');

        % define beta crystal symmetry
        CS = crystalSymmetry('m-3m', [3.192 3.192 3.192], 'mineral', 'Titanium Beta', 'color', 'light green');
        
        % analyse, plot and save beta texture
        [TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
        PF_001_max, PF_110_max, PF_111_max, odf] = beta_texture_plotter(user_inputs_filepath, inputDir.(stage), data_type,... 
                                                                                                phase, experiment_number_string, test_number.(stage), testFormat,... 
                                                                                                outputDir.(stage), output_text_file,....
                                                                                                CS, odf_max, odf_resolution, odf_misorientation,...
                                                                                                euler1, euler2, euler3,...
                                                                                                pf_max, pf_contour_step,...
                                                                                                odf_return)
    else
        disp('Phase not recognised.');
        return;
    end
    
    save odf variable as file
    save(strcat(outputDir.(stage),'/', phase, '_ODF.mat'), 'odf');
end

%% Plot the Texture Variation
% if strcmp(phase, 'alpha')
%     texture_variation_plot(outputDir, experiment_number_string, test_number, phase,... 
%                                         TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
%                                         PF_basal_max, PF_prismatic1_max, PF_prismatic2_max)
% 
% elseif strcmp(phase, 'beta')                                
%     texture_variation_plot(outputDir, experiment_number_string, test_number, phase,... 
%                                         TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
%                                         PF_001_max, PF_110_max, PF_111_max)                         
% end
