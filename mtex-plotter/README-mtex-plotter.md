MTEX Plotter
-----------

MTEX scripts for the batch processing of synchrotron intensity data that is written in spherical polar coordinate format. The scripts can be used for the automated analysis of alpha and beta phase crystallographic texture, plotting of pole figures, plotting of ODFs and calculation of texture strength values. 

The analysis folder will need to contain a number of different .txt files, recording the intensity distribution in spherical polar coordinates, for different lattice plane reflections.

Configuration .json files are used to record the input parameters. 

The user can click to navigate to the analysis and results folders using a GUI generated from the MTEX script, in the MATLAB console, and so file paths are not recorded in the configuration files. 

Contents
-----------
    
1. `sxrd_texture_plotter.m` A script for batch processing of synchrotron intensity data, to calculate texture, plot pole figures, plot ODFs and calculate texture strength values. It can currently be used for both alpha and beta phases in titanium alloys. But, it could easily be adapted for any phase in a crystal material.

2. `sxrd_texture_compare.m` A script for plotting the differences between ODFs, to compare an analysis ODF with a standard ODF.

MATLAB Setup
-----------

The scripts have been tested with MATLAB Version R2019b.

MTEX Installation
-----------

The MTEX toolbox can be downloaded from [here](https://mtex-toolbox.github.io/download), which also includes instructions for installing MTEX and troubleshooting any issues.

The scripts have been tested with MTEX Version 5.2.8, but should only require minor adjustments to work with future versions.

Some minor changes to the base MTEX code have been made to produce better looking figures. See [here](https://lightform-group.github.io/wiki/software_and_simulation/mtex-nice-figures) for more information.
