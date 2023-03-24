function [TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
PF_001_max, PF_110_max, PF_111_max, returned_odf] = beta_texture_plotter(user_inputs_filepath, inputDir, data_type,... 
                                                                                            phase, experiment_number_string, test_number, testFormat,... 
                                                                                            outputDir, output_text_file,....
                                                                                            CS, odf_max, odf_resolution, odf_misorientation,...
                                                                                            euler1, euler2, euler3,...
                                                                                            pf_max, pf_contour_step, ...
                                                                                            odf_return)                                                                                                                                                                           
% BETA_TEXTURE_PLOTTER
%   A function for the batch processing of synchrotron intensity data for
%   texture calculation, plotting of pole figures, plotting of ODFs and
%   calculation of texture strength values for the beta phase.
   
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
        
        if contains(user_inputs_filepath, 'config_diamond_2022')
            disp('Using 4 beta lattice plane peaks to refine beta texture.');
            % which files to be imported
            fname = { ...
              [pname '110.txt'],...
              [pname '200.txt'],...
              [pname '220.txt'],...
              [pname '310.txt'],...
              };

            % Specify Miller Indices
            h = { ...
              Miller(1,1,0,CS),...
              Miller(2,0,0,CS),...
              Miller(2,2,0,CS),...
              Miller(3,1,0,CS),...
              };
        
        elseif contains(user_inputs_filepath, 'config_diamond_2021')
            disp('Using 4 beta lattice plane peaks to refine beta texture.');
            % which files to be imported
            fname = { ...
              [pname '110.txt'],...
              [pname '200.txt'],...
              [pname '220.txt'],...
              [pname '310.txt'],...
              };

            % Specify Miller Indices
            h = { ...
              Miller(1,1,0,CS),...
              Miller(2,0,0,CS),...
              Miller(2,2,0,CS),...
              Miller(3,1,0,CS),...
              };
          
        elseif contains(user_inputs_filepath, 'config_diamond_2017')
            disp('Using 5 beta lattice plane peaks to refine beta texture.');
           
            % which files to be imported
            fname = { ...
              [pname '110.txt'],...
              [pname '200.txt'],...
              [pname '211.txt'],...
              [pname '220.txt'],...
              [pname '310.txt'],...
              };

            % Specify Miller Indices
            h = { ...
              Miller(1,1,0,CS),...
              Miller(2,0,0,CS),...
              Miller(2,1,1,CS),...
              Miller(2,2,0,CS),...
              Miller(3,1,0,CS),...
              };
                    
        elseif contains(user_inputs_filepath, 'config_desy_2021')
            disp('Using 4 beta lattice plane peaks to refine beta texture.');
           
            % which files to be imported
            fname = { ...
              [pname '110.txt'],...
              [pname '200.txt'],...
              [pname '220.txt'],...
              [pname '310.txt'],...
              };

            % Specify Miller Indices
            h = { ...
              Miller(1,1,0,CS),...
              Miller(2,0,0,CS),...
              Miller(2,2,0,CS),...
              Miller(3,1,0,CS),...
              };
          
        elseif contains(user_inputs_filepath, 'config_desy_2020')
            disp('Using 4 beta lattice plane peaks to refine beta texture.');
           
            % which files to be imported
            fname = { ...
              [pname '110.txt'],...
              [pname '200.txt'],...
              [pname '220.txt'],...
              [pname '310.txt'],...
              };

            % Specify Miller Indices
            h = { ...
              Miller(1,1,0,CS),...
              Miller(2,0,0,CS),...
              Miller(2,2,0,CS),...
              Miller(3,1,0,CS),...
              };
        else
            disp('JSON input filepath not currently recognised, need to define beta lattice plane peaks in `beta_texture_plotter.m` to refine beta texture.');
        end  

        % specify the number of indices
        number_of_indices = size(h)
        number_of_indices = number_of_indices(2)

        % Specify Specimen Symmetry
        % specimen symmetry
        SS = specimenSymmetry('triclinic'); % use for calculating pole figures
        %SS = specimenSymmetry('orthorhombic'); % use for calculating texture component volume fraction

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
        %plot(pf);
        %annotate([xvector,yvector],'label',{'RD','TD'},'backgroundcolor','w')
        %colorbar;

        % Calculate the ODF
        odf = calcODF(pf, 'RESOLUTION', odf_resolution);
        
        % Calculate the RP error value
        %RP_error(i) = calcError(pf, odf, 'RP')
        RP_error(i) = 0
        
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
        PF_001_max(i) = maxval(1);
        PF_110_max(i) = maxval(2);
        PF_111_max(i) = maxval(3);

        % Analyse the ODF
        
        % plot the ODF with orthorhombic symmetry by cropping ODF...
        
        specSym = 'orthorhombic';
        odf.SS=specimenSymmetry(specSym); % only crops the ODF at the moment
        
        % SS = specimenSymmetry(specSym);
        % odf = symmetrise_ODF(odf, CS, SS); % only works for one Fourier component
 
        % plot the ODF with orthorhombic symmetry by recalculating ODF...

        % Specify Specimen Symmetry
        % specimen symmetry
        %SS = specimenSymmetry('triclinic'); % use for calculating pole figures
        SS = specimenSymmetry('orthorhombic'); % use for calculating texture component volume fraction

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
        %plot(pf);
        %annotate([xvector,yvector],'label',{'RD','TD'},'backgroundcolor','w')
        %colorbar;

        % Calculate the ODF
        odf = calcODF(pf, 'RESOLUTION', odf_resolution);

        % Calculate the RP error value
        %RP_error(i) = calcError(pf, odf, 'RP')
        RP_error(i) = 0
        
        if (euler1 >0) || (euler2 > 0) || (euler3 > 0)
            % Rotate the ODF
            rot = rotation('Euler', euler1*degree, euler2*degree, euler3*degree);
            odf = rotate(odf,rot);
        else
            disp('ODF rotation not necessary.');
        end

        % plot the ODF slices
        output_filename = strcat(outputDir,'/',experiment_number_string,'_ODF_',test_number_string)
        ODF_plot(phase, odf, odf_max, output_filename, specSym);

        % calculate a value for the Texture Index
        disp('Calculating Texture Index.');
        TEXTURE_INDEX(i) = textureindex(odf);

        % calculate strength of ODF maxima
        disp('Calculating ODF maxima.');
        [odf_strength_max(i), odf_ori_max(i)] = max(odf)

        % record orientation of ODF maxima
        phi1(i) = odf_ori_max(i).phi1
        PHI(i) = odf_ori_max(i).Phi
        phi2(i) = odf_ori_max(i).phi2

        % define a texture component for the cubic phase
        cube = symmetrise(orientation.byEuler(45*degree,0*degree,45*degree,CS),'unique') % define component with Euler angles
        rotated_cube = symmetrise(orientation.byEuler(0*degree,0*degree,45*degree,CS),'unique')
        alpha_1 = orientation.byEuler(0*degree,10*degree,45*degree,CS) 
        alpha_2 = orientation.byEuler(0*degree,50*degree,45*degree,CS)
        gamma_1 = orientation.byEuler(0*degree,60*degree,45*degree,CS)
        gamma_2 = orientation.byEuler(90*degree,60*degree,45*degree,CS)
        
        alpha_fibre = fibre(alpha_1,alpha_2,'full')
        gamma_fibre = fibre(Miller(1,1,1,CS),vector3d.Z)
        
        % define the maximum possible misorientation
        misorientation = odf_misorientation*degree

        % separate a texture component and calculate the volume fraction
%         disp(['Calculating cube volume fraction for ', test_number_string]);
%         cube_volume_fraction(i) = volume(odf,cube,misorientation)*100
%         disp(['Calculating rotated cube volume fraction for ', test_number_string]);
%         rotated_cube_volume_fraction(i) = volume(odf,rotated_cube,misorientation)*100
%         disp(['Calculating alpha fibre volume fraction for ', test_number_string]);
%         alpha_fibre_volume_fraction(i) = volume(odf,alpha_fibre,misorientation)*100
%         disp(['Calculating gamma fibre volume fraction for ', test_number_string]);
%         gamma_fibre_volume_fraction(i) = volume(odf,gamma_fibre,misorientation)*100

        % write the texture values to file
%         fprintf(output_text_file, '%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n', test_number(i), TEXTURE_INDEX(i), odf_strength_max(i), rad2deg(phi1(i)), rad2deg(PHI(i)), rad2deg(phi2(i)), PF_001_max(i), PF_110_max(i), PF_111_max(i), cube_volume_fraction(i), rotated_cube_volume_fraction(i), alpha_fibre_volume_fraction(i), gamma_fibre_volume_fraction(i), RP_error(i))
        %fprintf(output_text_file, '%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n', test_number(i), TEXTURE_INDEX(i), odf_strength_max(i), rad2deg(phi1(i)), rad2deg(PHI(i)), rad2deg(phi2(i)), PF_001_max(i), PF_110_max(i), PF_111_max(i))
        
        % return ODF if requested
        if contains(odf_return, 'y') || contains(odf_return, 'Y') || contains(odf_return, 'yes') || contains(odf_return, 'YES')
            returned_odf = odf
        elseif contains(odf_return, 'n') || contains(odf_return, 'N') || contains(odf_return, 'no') || contains(odf_return, 'NO')   
            returned_odf = 0
        else
            disp('ODF return option not recognised.');
        end
    end
end
