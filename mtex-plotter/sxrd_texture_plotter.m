%% SXRD_TEXTURE_PLOTTER
% This script can be used  for the batch processing of synchrotron
% intensity data, written in spherical polar coordinate format.
% The script can be used for texture calculation, plotting of pole figures, 
% plotting of ODFs and calculation of texture strength values. 
% It can currently be used for both alpha and beta phases in titanium alloys.
% But, it could easily be adapted for any phase in any crystal alloy...

%% Define the user input configuration file

% Define the user input configuration file here...
% Note, this should be the only line you need to change in this script.
% Then you will be asked to select an input folder, containing  the
% intensity data files, and then asked to select an output folder, to save
% the ODFs, PFs and a text file containing the texture strength values.
user_inputs_filepath = 'json/config_diamond_2021_alpha.json'

%% Load user inputs from JSON file

% load the user inputs from JSON file
user_inputs = loadjson(user_inputs_filepath)

% specify the experiment number
experiment_number = user_inputs.experiment_number.value
experiment_number_characters = user_inputs.experiment_number.characters

% specify the test numbers
test_number_characters = user_inputs.test_number.characters

if strcmp(user_inputs_filepath, 'json/config_diamond_2021_alpha.json')
    disp('Using complex test number array.');
    test_number = [2:42 45:85 88:128 131:171 174:214 217:257 260:300 303:343 346:386];
elseif strcmp(user_inputs_filepath, 'json/config_diamond_2021_beta.json')
    disp('Using complex test number array.');
    test_number = [2:42 45:85 88:128 131:171 174:214 217:257 260:300 303:343 346:386];
else
    test_number_start = user_inputs.test_number.start
    test_number_end = user_inputs.test_number.end
    test_number_step = user_inputs.test_number.step
    test_number = test_number_start:test_number_step:test_number_end;
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

disp('Please navigate to the input directory, where the texture intensity data files are stored.');
inputDir = uigetdir; % gets input directory

disp('Please navigate to the output directory, where you would like to save the texture results.');
outputDir = uigetdir; % gets output directory

%% Specify Output

% define experiment number as a string
if experiment_number_characters == 3
    experiment_format_spec = '%03.f';
    experiment_number_string = num2str(experiment_number, experiment_format_spec)

elseif experiment_number_characters == 6
    experiment_format_spec = '%06.f';
    experiment_number_string = num2str(experiment_number, experiment_format_spec)
    
 else
    disp('Number of characters for experiment number not recognised.');
    return;
end

% define output path open file to save the texture values
output_text_file = fopen(fullfile(outputDir, strcat(experiment_number_string,'_texture_strength.txt')),'w')

%% Analyse Intensity Data

if test_number_characters == 3
    testFormat = '%03.f';

elseif test_number_characters == 5
    testFormat = '%05.f';
    
 else
    disp('Number of characters for test number not recognised.');
    return;
end
    
if strcmp(phase, 'alpha')
    % print header for alpha phase texture measurements
    fprintf(output_text_file, 'Test Number \t Texture Index \t ODF Max \t phi1 Angle of ODF Max \t PHI Angle of ODF Max \t phi2 Angle of ODF Max \t {0002} PF Max \t {10-10} PF Max \t {11-20} PF Max \t Basal TD Volume Fraction \t Basal RD Volume Fraction \n');
    
    % define alpha crystal symmetry
    CS = crystalSymmetry('6/mmm', [2.954 2.954 4.729], 'X||a*', 'Y||b', 'Z||c*', 'mineral', 'Titanium Alpha', 'color', 'light blue');
    [TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
    PF_basal_max, PF_prismatic1_max, PF_prismatic2_max] = alpha_texture_plotter(user_inputs_filepath, inputDir, outputDir, output_text_file, ....
                                                                                                   phase, experiment_number_string, test_number, testFormat,... 
                                                                                                   CS, odf_max, odf_resolution, odf_misorientation,...
                                                                                                   euler1, euler2, euler3,...
                                                                                                   pf_max, pf_contour_step)      
elseif strcmp(phase, 'beta')
    % print header for beta phase texture measurements
    fprintf(output_text_file, 'Test Number \t Texture Index \t ODF Max \t phi1 Angle of ODF Max \t PHI Angle of ODF Max \t phi2 Angle of ODF Max \t {001} PF Max \t {110} PF Max \t {111} PF Max \n');
    
    % define beta crystal symmetry
    CS = crystalSymmetry('m-3m', [3.192 3.192 3.192], 'mineral', 'Titanium Beta', 'color', 'light green');
    [TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
    PF_001_max, PF_110_max, PF_111_max] = beta_texture_plotter(user_inputs_filepath, inputDir, outputDir, output_text_file, ....
                                                                                                   phase, experiment_number_string, test_number, testFormat,... 
                                                                                                   CS, odf_max, odf_resolution, odf_misorientation,...
                                                                                                   euler1, euler2, euler3,...
                                                                                                   pf_max, pf_contour_step)
else
    disp('Phase not recognised.');
    return;
end

%% Plot the Texture Variation
if strcmp(phase, 'alpha')
    texture_variation_plot(outputDir, experiment_number_string, test_number, phase,... 
                                        TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
                                        PF_basal_max, PF_prismatic1_max, PF_prismatic2_max)

elseif strcmp(phase, 'beta')                                
    texture_variation_plot(outputDir, experiment_number_string, test_number, phase,... 
                                        TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
                                        PF_001_max, PF_110_max, PF_111_max)                         
end                 