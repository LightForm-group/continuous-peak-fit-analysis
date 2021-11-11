%% User Inputs...

% specify the experiment number
experiment_number = 065

% specify the test numbers
test_number = [3100:3400]

% specify the phase
phase = 'alpha'

% specify the plotting convention
setMTEXpref('xAxisDirection','north');
setMTEXpref('zAxisDirection','intoPlane');

% set the pole figure maxima
pf_max = 3
contour_step = 0.25

% specify the ODF resolution
odf_resolution = 10*degree

% set the ODF maxima
odf_max = 5

% specify rotation
euler1 = 90
euler2 = 0
euler3 = 0

%% Specify Crystal Symmetry

if strcmp(phase, 'alpha')
    % define alpha crystal symmetry
    CS = crystalSymmetry('6/mmm', [2.954 2.954 4.729], 'X||a*', 'Y||b', 'Z||c*', 'mineral', 'Titanium Alpha', 'color', 'light blue');
    
elseif strcmp(phase, 'beta')
    % define beta crystal symmetry
    CS = crystalSymmetry('m-3m', [3.192 3.192 3.192], 'mineral', 'Titanium Beta', 'color', 'light green');

else
    disp('Phase not recognised.');
    return;

end

%% Specify Output

% define experiment number
experiment_format_spec = '%03.f';
experiment_number_string = num2str(experiment_number, experiment_format_spec)

% define output path
output_path = strcat('/mnt/eps01-rds/Fonseca-Lightform/mbcx9cd4/SXRD_results/diamond_2017/', experiment_number_string,...
    '/texture-cpf/', experiment_number_string, '-raw-intensities-10deg/')

% open file to save the texture values
output_text_file = fopen(fullfile(output_path, strcat(experiment_number_string,'_texture_strength.txt')),'w')
fprintf(output_text_file, 'Test Number \t Texture Index \t ODF Max \t phi1 Angle of ODF Max \t PHI Angle of ODF Max \t phi2 Angle of ODF Max \t {0002} PF Max \t {10-10} PF Max \t {11-20} PF Max \t Basal TD Volume Fraction \t Basal RD Volume Fraction \n');

%% Analyse Intensity Data

for i = 1:length(test_number)
    
    % define test number
    test_format_spec = '%05.f';
    test_number_string = num2str(test_number(i),test_format_spec)
    
    % path to files
    pname = strcat('/mnt/eps01-rds/Fonseca-Lightform/mbcx9cd4/SXRD_analysis/diamond_2017/', experiment_number_string,...
        '/texture-cpf/', experiment_number_string, '-raw-intensities/', experiment_number_string, '_', test_number_string, '_peak_intensity_');
    
    % which files to be imported
    fname = { ...
      [pname '0002.txt'],...
      [pname '0004.txt'],...
      [pname '10-10.txt'],...
      [pname '10-11.txt'],...
      [pname '10-12.txt'],...
      [pname '10-14.txt'],...
      [pname '11-20.txt'],...
      [pname '11-22.txt'],...
      [pname '20-20.txt'],...
      [pname '20-21.txt'],...
      [pname '20-22.txt'],...
      };

    % Specify Miller Indices
    
    h = { ...
      Miller(0,0,0,2,CS),...
      Miller(0,0,0,4,CS),...
      Miller(1, 0,-1, 0,CS),...
      Miller(1, 0,-1, 1,CS),...
      Miller(1, 0,-1, 2,CS),...
      Miller(1, 0,-1, 4,CS),...
      Miller(1, 1,-2, 0,CS),...
      Miller(1, 1,-2, 2,CS),...
      Miller(2, 0,-2, 0,CS),...
      Miller(2, 0,-2, 1,CS),...
      Miller(2, 0,-2, 2,CS),...
      };
  
    % specify the number of indices
    number_of_indices = size(h)
    number_of_indices = number_of_indices(2)

    % Specify Specimen Symmetry
  
    % specimen symmetry
    SS = specimenSymmetry('triclinic');
  
    % Import the Data

    % create a Pole Figure variable containing the data
    pf = PoleFigure.load(fname,h,CS,SS,'interface','generic',...
      'ColumnNames', { 'Polar Angle' 'Azimuth Angle' 'Intensity'});

    % Correct Issue with pf.c Object
   
    % scale parameters for pf.c sometimes read as array of [1,1],
    % rather than array of 1 values, use command below 
    % to overwrite scale parameters.
    
    % pf.c = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
    sz = [1 number_of_indices]
    set_scale_params = ones(sz)
    pf.c = num2cell(set_scale_params)
  
    % Plot the Intensity Distibrutions

    % plot(pf);
    % annotate([xvector,yvector],'label',{'RD','TD'},'backgroundcolor','w')
    % colorbar;

    % Calculate the ODF

    odf = calcODF(pf, 'RESOLUTION', odf_resolution);

    % Rotate the ODF
    
    rot = rotation('Euler', euler1*degree, euler2*degree, euler3*degree);
    odf = rotate(odf,rot);
    
    % Plot the Pole Figures with Contouring 

    % plot the pole figure
    output_filename = strcat(output_path,experiment_number_string,'_PF_',test_number_string)
    [maxval] = pole_figure_plot(phase, odf, CS, contour_step, pf_max, output_filename);
    PF_basal_max(i) = maxval(1);
    PF_prismatic1_max(i) = maxval(2);
    PF_prismatic2_max(i) = maxval(3);
    
    % Analyse the ODF
    
    % plot the ODF with orthorhombic symmetry
    odf.SS=specimenSymmetry('orthorhombic');
    specSym = 'orthorhombic';
    output_filename = strcat(output_path,experiment_number_string,'_ODF_',test_number_string)
    ODF_plot(phase, odf, odf_max, output_filename, specSym);

    % calculate a value for the Texture Index
    TEXTURE_INDEX(i) = textureindex(odf);

    % calculate strength of ODF maxima
    [odf_strength_max(i), odf_ori_max(i)] = max(odf)

    % record orientation of ODF maxima
    phi1(i) = odf_ori_max(i).phi1
    PHI(i) = odf_ori_max(i).Phi
    phi2(i) = odf_ori_max(i).phi2

    % define a texture component for the hexagonal phase
    basal_TD = symmetrise(orientation.byEuler(0*degree,90*degree,0*degree,CS),'unique') % define component with Euler angles
    basal_RD = symmetrise(orientation.byEuler(90*degree,90*degree,0*degree,CS),'unique')

    % define the maximum possible misorientation
    misorientation = 5*degree
    
    % seperate a texture component and calculate the volume fraction
    %basal_TD_volume_fraction(i) = volume(odf, basal_TD,misorientation)
    %basal_RD_volume_fraction(i) = volume(odf, basal_RD,misorientation)
    
    % write the texture values to file
    %fprintf(output_text_file, '%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n', test_number(i), TEXTURE_INDEX(i), odf_strength_max(i), rad2deg(phi1(i)), rad2deg(PHI(i)), rad2deg(phi2(i)), PF_basal_max(i), PF_prismatic1_max(i), PF_prismatic2_max(i), basal_TD_volume_fraction(i), basal_RD_volume_fraction(i))
    fprintf(output_text_file, '%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n', test_number(i), TEXTURE_INDEX(i), odf_strength_max(i), rad2deg(phi1(i)), rad2deg(PHI(i)), rad2deg(phi2(i)), PF_basal_max(i), PF_prismatic1_max(i), PF_prismatic2_max(i))
    
end

%% Close any Open Files

fclose(output_text_file)

%% Plot the Texture Variation

i = 1:length(test_number)

TEXTURE_INDEX_figure = figure();
hold on
plot(i,TEXTURE_INDEX,'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('Texture Index')
hold off
legend('Texture Index')
saveas (TEXTURE_INDEX_figure, strcat(output_path,experiment_number_string,'_TI_line_plot.png'));

odf_max_figure = figure();
hold on
plot(i,odf_strength_max,'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('ODF Maximum')
hold off
legend('ODF Maximum')
saveas (odf_max_figure, strcat(output_path,experiment_number_string,'_odf_max_line_plot.png'));

phi1_figure = figure();
hold on
plot(i,rad2deg(phi1),'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('Phi1 Angle')
hold off
legend('Phi1 Angle')
saveas (phi1_figure, strcat(output_path,experiment_number_string,'_phi1_line_plot.png'));

PHI_figure = figure();
hold on
plot(i,rad2deg(PHI),'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('PHI Angle')
hold off
legend('PHI Angle')
saveas (PHI_figure, strcat(output_path,experiment_number_string,'_PHI_line_plot.png'));

phi2_figure = figure();
hold on
plot(i,rad2deg(phi2),'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('Phi2 Angle')
hold off
legend('Phi2 Angle')
saveas (phi2_figure, strcat(output_path,experiment_number_string,'_phi2_line_plot.png'));

PF_basal_figure = figure();
hold on
plot(i,PF_basal_max,'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('{0002} Pole Figure Max.')
hold off
legend('{0002} Pole Figure Max.')
saveas (PF_basal_figure, strcat(output_path,experiment_number_string,'_PF_basal_line_plot.png'));

PF_prismatic1_figure = figure();
hold on
plot(i,PF_prismatic1_max,'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('{10-10} Pole Figure Max.')
hold off
legend('{10-10} Pole Figure Max.')
saveas (PF_prismatic1_figure, strcat(output_path,experiment_number_string,'_PF_prismatic1_line_plot.png'));

PF_prismatic2_figure = figure();
hold on
plot(i,PF_prismatic2_max,'Color',[1,0,0],'lineWidth',2) % red;
xlabel('Slice Number')
ylabel('{11-20} Pole Figure Max.')
hold off
legend('{11-20} Pole Figure Max.')
saveas (PF_prismatic2_figure, strcat(output_path,experiment_number_string,'_PF_prismatic2_line_plot.png'));