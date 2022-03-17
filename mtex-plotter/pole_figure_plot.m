function [maxval] = pole_figure_plot(phase, ori, CS, contour_step, pf_max, output_filename);
% POLE_FIGURE_PLOT
%   A function for plotting alpha (hexagonal close-packed) or beta
%   (body-centred-cubic) pole figures using MTEX

  if strcmp(phase, 'alpha');
    PF = figure();
    hkil = [Miller(0,0,0,2,ori.CS), Miller(1,0,-1,0,ori.CS), Miller(1,1,-2,0,ori.CS)]; % include hkil figures here
    plotPDF(ori, hkil,'antipodal', 'contourf', 0:contour_step:pf_max, 'minmax') % plot with contouring
    %plotPDF(ori, hkil, 'antipodal', 'minmax'); % plot without contouring
    text(vector3d.X, 'RD', 'VerticalAlignment', 'bottom'); % moving the vector3d axis labels outside of the hemisphere boundary
    text(vector3d.Y, 'TD', 'horizontalAlignment', 'left');
    f = gcm; % moving up the hkil labels to make room for the rolling direction labels
    
    for i = 1:length(f.children)
        f.children(i).Title.Position=[1,1.25,1]; % use [-1,1.25,1] to make layout similar to Channel 5 and turn off minmax if you want to
        ax = getappdata(f.children(i),'sphericalPlot');
        minval(i) = ax.minData;
        maxval(i) = ax.maxData;
    end
    
    CLim(gcm,[0 pf_max]); % define a colour giving the range (gcm, [min, max])
    mtexColorbar ('location', 'southoutside', 'title', 'mrd'); % move colorbar to horizontal to avoid overlap
    set(gcf, 'PaperPositionMode', 'auto');
    saveas (PF, output_filename, 'png');
    close(PF);

  elseif strcmp(phase, 'beta');
    PF = figure();
    hkil = [Miller(0,0,1,ori.CS), Miller(1,1,0,ori.CS), Miller(1,1,1,ori.CS)]; % include hkil figures here
    plotPDF(ori, hkil,'antipodal', 'contourf', 0:contour_step:pf_max, 'minmax') % plot with contouring
    %plotPDF(ori, hkil, 'antipodal', 'minmax'); % plot without contouring
    text(vector3d.X, 'RD', 'VerticalAlignment', 'bottom'); % moving the vector3d axis labels outside of the hemisphere boundary
    text(vector3d.Y, 'TD', 'horizontalAlignment', 'left');
    f = gcm; % moving up the hkil labels to make room for the rolling direction labels
    
    for i = 1:length(f.children)
        f.children(i).Title.Position=[1,1.25,1]; % use [-1,1.25,1] to make layout similar to Channel 5 and turn off minmax if you want to
        ax = getappdata(f.children(i),'sphericalPlot');
        minval(i) = ax.minData;
        maxval(i) = ax.maxData;
    end
    
    CLim(gcm,[0 pf_max]); % define a colour giving the range (gcm, [min, max])
    mtexColorbar ('location', 'southoutside', 'title', 'mrd'); % move colorbar to horizontal to avoid overlap
    set(gcf, 'PaperPositionMode', 'auto');
    saveas (PF, output_filename, 'png');
    close(PF);
    
  else 
    disp ('Phase not recognised for plotting pole figures.');
    return;
  end
  
end