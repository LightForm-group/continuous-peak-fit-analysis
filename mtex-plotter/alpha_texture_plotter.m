function [TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
PF_basal_max, PF_prismatic1_max, PF_prismatic2_max] = alpha_texture_plotter(user_inputs_filepath, inputDir, data_type,... 
                                                                                            phase, experiment_number_string, test_number, testFormat,... 
                                                                                            outputDir, output_text_file,....
                                                                                            CS, odf_max, odf_resolution, odf_misorientation,...
                                                                                            euler1, euler2, euler3,...
                                                                                            pf_max, pf_contour_step)                                                                                                                                                                           
% ALPHA_TEXTURE_PLOTTER
%   A function for the batch processing of synchrotron intensity data for
%   texture calculation, plotting of pole figures, plotting of ODFs and
%   calculation of texture strength values for the alpha phase.
    
    for i = 1:length(test_number)
        % define test number
        test_number_string = num2str(test_number(i), testFormat)
        
        if strcmp(data_type, 'individual')
            % path to files
            pname = strcat(inputDir, '/', experiment_number_string, '_', test_number_string, '_peak_intensity_');
        
        elseif strcmp(data_type, 'summed')
            % path to files
            pname = strcat(inputDir, '/', experiment_number_string, '_summed_', test_number_string, '_peak_intensity_');

        elseif strcmp(data_type, 'combined')
            % path to files
            pname = strcat(inputDir, '/combined_', test_number_string, '_peak_intensity_');
            experiment_number_string = 'combined'
        else
            disp('Date type not recognised, choose from individual, summed, or combined');
        end
              
        if contains(user_inputs_filepath, 'json/config_diamond_2021')
            disp('Using 21 alpha lattice plane peaks to refine alpha texture.');
            % which files to be imported
            fname = { ...
              [pname '0002.txt'],...
              [pname '0004.txt'],...
              [pname '10-10.txt'],...
              [pname '10-11.txt'],...
              [pname '10-12.txt'],...
              [pname '10-13.txt'],...
              [pname '10-14.txt'],...
              [pname '10-15.txt'],...
              [pname '11-20.txt'],...
              [pname '11-22.txt'],...
              [pname '11-24.txt'],...
              [pname '20-20.txt'],...
              [pname '20-21.txt'],...
              [pname '20-22.txt'],...
              [pname '20-23.txt'],...
              [pname '20-24.txt'],...
              [pname '21-30.txt'],...
              [pname '21-31.txt'],...
              [pname '21-32.txt'],...
              [pname '30-30.txt'],...
              [pname '30-31.txt'],...
              };

            % Specify Miller Indices
            h = { ...
              Miller(0,0,0,2,CS),...
              Miller(0,0,0,4,CS),...
              Miller(1, 0,-1, 0,CS),...
              Miller(1, 0,-1, 1,CS),...
              Miller(1, 0,-1, 2,CS),...
              Miller(1, 0,-1, 3,CS),...
              Miller(1, 0,-1, 4,CS),...
              Miller(1, 0,-1, 5,CS),...
              Miller(1, 1,-2, 0,CS),...
              Miller(1, 1,-2, 2,CS),...
              Miller(1, 1,-2, 4,CS),...
              Miller(2, 0,-2, 0,CS),...
              Miller(2, 0,-2, 1,CS),...
              Miller(2, 0,-2, 2,CS),...
              Miller(2, 0,-2, 3,CS),...
              Miller(2, 0,-2, 4,CS),...
              Miller(2, 1,-3, 0,CS),...
              Miller(2, 1,-3, 1,CS),...
              Miller(2, 1,-3, 2,CS),...
              Miller(3, 0,-3, 0,CS),...
              Miller(3, 0,-3, 1,CS),...
              };
        
        elseif contains(user_inputs_filepath, 'json/config_diamond_2017')
            disp('Using 11 alpha lattice plane peaks to refine alpha texture.');
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
          
        elseif contains(user_inputs_filepath, 'json/config_desy_2021')
            disp('Using 14 alpha lattice plane peaks to refine alpha texture.');
            % which files to be imported
            fname = { ...
              [pname '0002.txt'],...
              [pname '0004.txt'],...
              [pname '10-10.txt'],...
              [pname '10-11.txt'],...
              [pname '10-12.txt'],...
              [pname '10-13.txt'],...
              [pname '10-14.txt'],...
              [pname '11-20.txt'],...
              [pname '11-22.txt'],...
              [pname '20-20.txt'],...
              [pname '20-21.txt'],...
              [pname '20-22.txt'],...
              [pname '20-23.txt'],...
              [pname '21-30.txt'],...
              };

            % Specify Miller Indices
            h = { ...
              Miller(0,0,0,2,CS),...
              Miller(0,0,0,4,CS),...
              Miller(1, 0,-1, 0,CS),...
              Miller(1, 0,-1, 1,CS),...
              Miller(1, 0,-1, 2,CS),...
              Miller(1, 0,-1, 3,CS),...
              Miller(1, 0,-1, 4,CS),...
              Miller(1, 1,-2, 0,CS),...
              Miller(1, 1,-2, 2,CS),...
              Miller(2, 0,-2, 0,CS),...
              Miller(2, 0,-2, 1,CS),...
              Miller(2, 0,-2, 2,CS),...
              Miller(2, 0,-2, 3,CS),...
              Miller(2, 1,-3, 0,CS),...
              };  
        else
            disp('JSON input filepath not currently recognised, need to define alpha lattice plane peaks in `alpha_texture_plotter.m` to refine alpha texture.');
        end
        
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
        % to overwrite any incorrect scale parameters, such as
        % pf.c = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}

        sz = [1 number_of_indices]
        set_scale_params = ones(sz)
        pf.c = num2cell(set_scale_params)

        % Plot the Intensity Distributions
        % plot(pf);
        % annotate([xvector,yvector],'label',{'RD','TD'},'backgroundcolor','w')
        % colorbar;

        % Calculate the ODF
        odf = calcODF(pf, 'RESOLUTION', odf_resolution);

        if (euler1 >0) || (euler2 > 0) || (euler3 > 0)
            % Rotate the ODF
            rot = rotation('Euler', euler1*degree, euler2*degree, euler3*degree);
            odf = rotate(odf,rot);
        else
            disp('ODF rotation not necessary.');
        end
        
        % Plot the Pole Figures with Contouring 
        % plot the pole figure
        output_filename = strcat(outputDir,'/',experiment_number_string,'_PF_',test_number_string)
        [maxval] = pole_figure_plot(phase, odf, CS, pf_contour_step, pf_max, output_filename);
        PF_basal_max(i) = maxval(1);
        PF_prismatic1_max(i) = maxval(2);
        PF_prismatic2_max(i) = maxval(3);

        % Analyse the ODF
        % plot the ODF with orthorhombic symmetry
        odf.SS=specimenSymmetry('orthorhombic');
        specSym = 'orthorhombic';
        output_filename = strcat(outputDir,'/',experiment_number_string,'_ODF_',test_number_string)
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
        misorientation = odf_misorientation*degree

        % seperate a texture component and calculate the volume fraction
        %basal_TD_volume_fraction(i) = volume(odf, basal_TD,misorientation)
        %basal_RD_volume_fraction(i) = volume(odf, basal_RD,misorientation)

        % write the texture values to file
        %fprintf(output_text_file, '%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n', test_number(i), TEXTURE_INDEX(i), odf_strength_max(i), rad2deg(phi1(i)), rad2deg(PHI(i)), rad2deg(phi2(i)), PF_basal_max(i), PF_prismatic1_max(i), PF_prismatic2_max(i), basal_TD_volume_fraction(i), basal_RD_volume_fraction(i))
        fprintf(output_text_file, '%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n', test_number(i), TEXTURE_INDEX(i), odf_strength_max(i), rad2deg(phi1(i)), rad2deg(PHI(i)), rad2deg(phi2(i)), PF_basal_max(i), PF_prismatic1_max(i), PF_prismatic2_max(i))
    end
end
