function [] = texture_variation_plot(outputDir, experiment_number_string, test_number, phase,... 
                                                        TEXTURE_INDEX, odf_strength_max, phi1, PHI, phi2,...
                                                        PF1_max, PF2_max, PF3_max)
%TEXTURE_VARIATION_PLOT
%   A function for plotting texture variation with image number, for a
%   number of different texture strength variables, including the texture
%   index, ODF maxima, phi1, PHI and phi2 angles, as well as the maxima
%  from three different lattice plane pole figures.

    if strcmp(phase, 'alpha');

        PF_basal_max = PF1_max
        PF_prismatic1_max = PF2_max
        PF_prismatic2_max = PF3_max
        
        i = 1:length(test_number)

        TEXTURE_INDEX_figure = figure();
        hold on
        plot(i,TEXTURE_INDEX,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('Texture Index')
        hold off
        legend('Texture Index')
        saveas (TEXTURE_INDEX_figure, strcat(outputDir,'/',experiment_number_string,'_TI_line_plot.png'));

        odf_max_figure = figure();
        hold on
        plot(i,odf_strength_max,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('ODF Maximum')
        hold off
        legend('ODF Maximum')
        saveas (odf_max_figure, strcat(outputDir,'/',experiment_number_string,'_odf_max_line_plot.png'));

        phi1_figure = figure();
        hold on
        plot(i,rad2deg(phi1),'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('Phi1 Angle')
        hold off
        legend('Phi1 Angle')
        saveas (phi1_figure, strcat(outputDir,'/',experiment_number_string,'_phi1_line_plot.png'));

        PHI_figure = figure();
        hold on
        plot(i,rad2deg(PHI),'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('PHI Angle')
        hold off
        legend('PHI Angle')
        saveas (PHI_figure, strcat(outputDir,'/',experiment_number_string,'_PHI_line_plot.png'));

        phi2_figure = figure();
        hold on
        plot(i,rad2deg(phi2),'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('Phi2 Angle')
        hold off
        legend('Phi2 Angle')
        saveas (phi2_figure, strcat(outputDir,'/',experiment_number_string,'_phi2_line_plot.png'));

        PF_basal_figure = figure();
        hold on
        plot(i,PF_basal_max,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('{0002} Pole Figure Max.')
        hold off
        legend('{0002} Pole Figure Max.')
        saveas (PF_basal_figure, strcat(outputDir,'/',experiment_number_string,'_PF_basal_line_plot.png'));

        PF_prismatic1_figure = figure();
        hold on
        plot(i,PF_prismatic1_max,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('{10-10} Pole Figure Max.')
        hold off
        legend('{10-10} Pole Figure Max.')
        saveas (PF_prismatic1_figure, strcat(outputDir,'/',experiment_number_string,'_PF_prismatic1_line_plot.png'));

        PF_prismatic2_figure = figure();
        hold on
        plot(i,PF_prismatic2_max,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('{11-20} Pole Figure Max.')
        hold off
        legend('{11-20} Pole Figure Max.')
        saveas (PF_prismatic2_figure, strcat(outputDir,'/',experiment_number_string,'_PF_prismatic2_line_plot.png'));

    elseif strcmp(phase, 'beta')

        PF_001_max = PF1_max
        PF_110_max = PF2_max
        PF_111_max = PF3_max

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

        PF_001_figure = figure();
        hold on
        plot(i,PF_001_max,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('{001} Pole Figure Max.')
        hold off
        legend('{001} Pole Figure Max.')
        saveas (PF_001_figure, strcat(output_path,experiment_number_string,'_PF_001_line_plot.png'));

        PF_110_figure = figure();
        hold on
        plot(i,PF_110_max,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('{110} Pole Figure Max.')
        hold off
        legend('{110} Pole Figure Max.')
        saveas (PF_110_figure, strcat(output_path,experiment_number_string,'_PF_110_line_plot.png'));

        PF_111_figure = figure();
        hold on
        plot(i,PF_111_max,'Color',[1,0,0],'lineWidth',2) % red;
        xlabel('Slice Number')
        ylabel('{111} Pole Figure Max.')
        hold off
        legend('{111} Pole Figure Max.')
        saveas (PF_111_figure, strcat(output_path,experiment_number_string,'_PF_111_line_plot.png'));

    else 
        disp ('Phase not recognised for plotting pole figures.');
        return;
    end
end
