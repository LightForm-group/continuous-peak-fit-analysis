continuous-peak-fit-analysis
-----------

A Python package for fitting full synchrotron X-ray diffraction (SXRD) pattern rings to analyse texture (intensity) and elastic lattice strain (position) changes. Uses the Continuous-Peak-Fit Python package for fitting the azimuth and time dependency of peaks with Fourier Series descriptions.

The notebooks can be used to setup and run Continuous-Peak-Fit analyses, and to analyse the resulting peak profile fits from a series of SXRD pattern images, to directly extract the material crystallographic properties. The peak profile changes, such as intensity and peak position, can be used to discern material changes, such as crystallographic texture and elastic lattice strain, which are guided by the notebooks. There is an option to combine the diffraction results with bulk behaviour measurements using external thermomechanical testing equipment.

The package includes a separate folder of MTEX scripts, in MATLAB, for automatic analysis of the lattice plane intensities produced from Continuous-Peak-Fit, to calculate orientation distribution functions (ODFs), calculate texture intensity values and plot pole figures. More details about the setup of MTEX can be found in mtex-plotter/README-mtex-plotter.md

Development
--------------

This package was developed by Christopher S. Daniel at The 
University of Manchester, UK, and was funded by the Engineering and Physical Sciences Research Council (EPSRC) via the LightForm programme grant (EP/R001715/1). LightForm is a 5 year multidisciplinary project, led by The Manchester University with partners at University of Cambridge and Imperial College, London (https://lightform.org.uk/).

Contents
-----------

**It is recommended the user works through the example notebooks in the following order:**
    
1. `Ti64_continuous_peak_fit_RUN.ipynb` A notebook for setting up and running Continuous-Peak-Fit to fit full lattice plane rings.

2. `notebooks/NOTES_intensity_circles_to_polar_coordinates.ipynb` An interactive guide explaining how to calculate polar coordinates for plotting of intensity circles in 3D (as pole figures).

3. `notebooks/Ti64_continuous_peak_fit_TEXTURE_ANALYSIS.ipynb` A notebook for anlaysing crystallographic texture from the Continuous-Peak-Fit output. Extracts lattice plane intensity distributions from the .fit files, to rewrite them in a spherical polar coordinate .txt format that can be analysed using MTEX.

4. `notebooks/Ti64_continous_peak_fit_DEFORMATION_ANALYSIS.ipynb` A notebook for analysing micromechanical deformation from the Continuous-Peak-Fit output. The notebook can be used to plot the intensity, peak-width, and peak position, which can be combined with external measurements from thermomechanical testing equipment.

*Note, the `example-data/` and `example-analysis/` folders contain instuctions for downloading data that can be used as an example analysis, but a clear external file structure should be setup to support the analysis of large synchrotron datasets.*

Installation and Virtual Environment Setup
-----------

Follow along by copying / pasting the commands below into your terminal (for a guide on using a python virtual environments follow steps 4-7).

**1. First, you'll need to download the repository to your PC. Open a unix command line on your PC and navigate to your Desktop (or GitHub repository):**
```unix
cd ~/Desktop
```
**2. In your teminal, use the following command to clone this repository to your Desktop:**
```unix
git clone https://github.com/LightForm-group/continuous-peak-fit-analysis.git
```
**3. Navigate inside `Desktop/continuous-peak-fit-analysis/` and list the contents using `ls`(macOS) or `dir`(windows):**
```unix
cd ~/Desktop/continuous-peak-fit-analysis/
```
**4. Next, create a python virtual environment (venv) which contains all of the python libraries required to use continuous-peak-fit-analysis.
Firstly, use the following command to create the venv directory which will contain the necessary libraries:**
```unix
python -m venv ~/Desktop/continuous-peak-fit-analysis/venv
```
**5. Your `continuous-peak-fit-analysis/` directory should now contain `venv/`. Install the relevant libraries to this venv by first activating the venv:**
```unix
source ~/Desktop/continuous-peak-fit-analysis/venv/bin/activate
```
*Note, the beginning of your command line should change from `(base)` to include `(venv)`.*

**6. Install the python libraries to this virtual environment using pip and the `requirements.txt` file included within the repository:**
```unix
pip install -r ~/Desktop/continuous-peak-fit-analysis/requirements.txt
```
**7. To ensure these installed correctly, use the command `pip list` and ensure the following packages are installed:**
```unix
pip list
# Check to ensure that all of the following are listed:
#jupyter
#matplotlib
#lmfit
#h5py
#pillow
#pyFAI
#pyyaml
#tqdm
```
**8. If all in step 7 are present, you can now run the example notebooks.
Ensure the venv is active and use the following command to boot jupyter notebook (using all libraries installed in the venv).
Warning - using just `jupyter notebook` without `python -m` can result in using your default python environment (the libraries may not be recognised):**
```unix
python -m jupyter notebook
```
**9. Work through the notebooks and setup yaml text files for reproducible crystallographic texture and micromechanical deformation analysis of large synchrotron datasets.**

**10. When you're finished using the virtual environment, deactivate it!
This will avoid confusion when using different python libraries that are not installed within the virtual environment:**
```unix
deactivate
```

Required Libraries
--------------------

The required libraries are listed in requirements.txt