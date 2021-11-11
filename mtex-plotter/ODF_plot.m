function [  ] = ODF_plot(phase, odf, odf_max, output_filename, specSym);
% A function for plotting slices of the alpha (hexagonal close-packed) or beta (body-centred-cubic) ODF using MTEX

  if strcmp(phase, 'alpha');
    ODF_fig = figure();
    plot(odf, 'PHI2', [0 15 30]*degree);
    CLim(gcm,[0,odf_max]); % define a colour giving the range (gcm, [min, max])
    mtexColorbar ('location', 'southoutside', 'title', 'mrd'); % move colorbar to horizontal to avoid any overlap
    set(gcf, 'PaperPositionMode', 'auto');
    if strcmp(specSym, 'orthorhombic')
      saveas (ODF_fig, strcat(output_filename, '_orthorhombic'), 'png');
    elseif strcmp(specSym, 'triclinic')
      saveas (ODF_fig, strcat(output_filename, '_triclinic'), 'png');
    else 
      disp('specSym not satisfied - choose orthorhombic or triclinic');
    end
    close(ODF_fig);
  
  elseif strcmp(phase, 'beta');
    ODF_fig = figure();
    plot(odf, 'PHI2', [0 45]*degree);
    CLim(gcm,[0,odf_max]); % define a colour giving the range (gcm, [min, max])
    mtexColorbar ('location', 'southoutside', 'title', 'mrd'); % move colorbar to horizontal to avoid any overlap
    set(gcf, 'PaperPositionMode', 'auto');
    if strcmp(specSym, 'orthorhombic')
      saveas (ODF_fig, strcat(output_filename, '_orthorhombic'), 'png');
    elseif strcmp(specSym, 'triclinic')
      saveas (ODF_fig, strcat(output_filename, '_triclinic'), 'png');
    else 
      disp('specSym not satisfied - choose orthorhombic or triclinic');
    end
    close(ODF_fig);
    
  else 
    disp ('Phase not recognised for plotting ODF slices.'); 
    return;
  end
end