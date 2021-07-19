# Input parameters for Ti64

# data drive.
import os 
drive = "D:/Chris Daniel/"

# properties of the data files.
datafile_directory = drive + 'Continuous-Peak-Fit-Analysis/example-data/Diamond_2017/065_tiff_images'
datafile_Basename  = "pixium_"
datafile_Ending    = ".tif"
datafile_StartNum  = 3100
datafile_EndNum    = 3400
datafile_NumDigit  = 5

# calibration and masking.
Calib_type   = "Dioptas"
Calib_detector = 'unknown'
Calib_data     = drive + 'Continuous-Peak-Fit-Analysis/example-calibration/Diamond_2017/pixi_00001.tif'
Calib_param    = 'example-calibration/Diamond_2017/DLS_CeO2_1200mm.poni'
Calib_mask     = 'example-calibration/Diamond_2017/DLS_CeO2_1200mm.mask'
Calib_pixels = 296


# number of bins for initial fitting.
AziBins = 90


# fitting properties for peaks.
fit_orders = [
       {
         "range": [[3.00, 3.25]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '100',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[3.35, 3.65]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '002',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64beta",
             "hkl": '110',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '101',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,3.38],
                                    [1,-58.997,3.38],
                                    [1,59.289,3.38],
                                    [1,23.187,3.38],
                                    [1,23.212,3.38], 
                                    [1,23.158,3.38], 
                                    [1,123.246,3.38],
                                    [2,-120.5,3.44],
                                    [2,-58.997,3.44],
                                    [2,59.289,3.44],
                                    [2,23.187,3.44],
                                    [2,23.212,3.44], 
                                    [2,23.158,3.44], 
                                    [2,123.246,3.44],
                                    [3,-120.5,3.55],
                                    [3,-58.997,3.55],
                                    [3,59.289,3.55],
                                    [3,23.187,3.55],
                                    [3,23.212,3.55], 
                                    [3,23.158,3.55], 
                                    [3,123.246,3.55]]
       },
       {
         "range": [[4.50, 4.70]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '102',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[4.75, 4.95]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64beta",
             "hkl": '200',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[5.30, 5.50]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '110',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[5.85, 6.05]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '103',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[6.10, 6.65]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '200',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '112',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '201',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,6.25],
                                    [1,-58.997,6.25],
                                    [1,59.289,6.25],
                                    [1,23.187,6.25],
                                    [1,23.212,6.25], 
                                    [1,23.158,6.25], 
                                    [1,123.246,6.25],
                                    [2,-120.5,6.37],
                                    [2,-58.997,6.37],
                                    [2,59.289,6.37],
                                    [2,23.187,6.37],
                                    [2,23.212,6.37], 
                                    [2,23.158,6.37], 
                                    [2,123.246,6.37],
                                    [3,-120.5,6.47],
                                    [3,-58.997,6.47],
                                    [3,59.289,6.47],
                                    [3,23.187,6.47],
                                    [3,23.212,6.47], 
                                    [3,23.158,6.47], 
                                    [3,123.246,6.47]]
       },
       {
         "range": [[6.60, 7.20]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '004',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64beta",
             "hkl": '220',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '202',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,6.75],
                                    [1,-58.997,6.75],
                                    [1,59.289,6.75],
                                    [1,23.187,6.75],
                                    [1,23.212,6.75], 
                                    [1,23.158,6.75], 
                                    [1,123.246,6.75],
                                    [2,-120.5,6.88],
                                    [2,-58.997,6.88],
                                    [2,59.289,6.88],
                                    [2,23.187,6.88],
                                    [2,23.212,6.88], 
                                    [2,23.158,6.88], 
                                    [2,123.246,6.88],
                                    [3,-120.5,7.10],
                                    [3,-58.997,7.10],
                                    [3,59.289,7.10],
                                    [3,23.187,7.10],
                                    [3,23.212,7.10], 
                                    [3,23.158,7.10], 
                                    [3,123.246,7.10]]
       },
    ]

# output settings
Output_directory   = './'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360