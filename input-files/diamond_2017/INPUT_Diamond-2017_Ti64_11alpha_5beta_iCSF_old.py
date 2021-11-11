# Input parameters for Ti64

# data drive.
import os 
drive = "/mnt/iusers01/jf01/mbcx9cd4/rds_lightform/"

# properties of the data files.
datafile_directory = drive + 'SXRD_raw_data/diamond_2017/rawdata/065_TI64_NDload_900C_15mms_25_02_2017-103832/'
datafile_Basename  = "pixium_"
datafile_Ending    = ".tif"
datafile_StartNum  = 3100
datafile_EndNum    = 3400
datafile_NumDigit  = 5

# calibration and masking.
Calib_type   = "Dioptas"
Calib_detector = 'unknown'
Calib_data     = drive + 'SXRD_analysis/diamond_2017/calibration-dioptas/pixi_00001.tif'
Calib_param    = drive + 'SXRD_analysis/diamond_2017/calibration-dioptas/DLS_CeO2_1200mm.poni'
Calib_mask     = drive + 'SXRD_analysis/diamond_2017/calibration-dioptas/DLS_CeO2_1200mm.mask'
Calib_pixels = 296


# number of bins for initial fitting.
AziBins = 90


# fitting properties for peaks.
fit_orders = [
       {
         "range": [[3.05, 3.20]],
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
         "range": [[3.30, 3.68]],
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
         "range": [[4.48, 4.73]],
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
         "range": [[4.74, 5.00]],
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
         "range": [[5.29, 5.56]],
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
         "range": [[5.82, 6.11]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64beta",
             "hkl": '211',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[6.13, 6.59]],
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
                                    [2,-120.5,6.38],
                                    [2,-58.997,6.38],
                                    [2,59.289,6.38],
                                    [2,23.187,6.38],
                                    [2,23.212,6.38], 
                                    [2,23.158,6.38], 
                                    [2,123.246,6.38],
                                    [3,-120.5,6.47],
                                    [3,-58.997,6.47],
                                    [3,59.289,6.47],
                                    [3,23.187,6.47],
                                    [3,23.212,6.47], 
                                    [3,23.158,6.47], 
                                    [3,123.246,6.47]]
       },
       {
         "range": [[6.66, 7.20]],
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
          "PeakPositionSelection": [[1,-120.5,6.77],
                                    [1,-58.997,6.77],
                                    [1,59.289,6.77],
                                    [1,23.187,6.77],
                                    [1,23.212,6.77], 
                                    [1,23.158,6.77], 
                                    [1,123.246,6.77],
                                    [2,-120.5,6.88],
                                    [2,-58.997,6.88],
                                    [2,59.289,6.88],
                                    [2,23.187,6.88],
                                    [2,23.212,6.88], 
                                    [2,23.158,6.88], 
                                    [2,123.246,6.88],
                                    [3,-120.5,7.11],
                                    [3,-58.997,7.11],
                                    [3,59.289,7.11],
                                    [3,23.187,7.11],
                                    [3,23.212,7.11], 
                                    [3,23.158,7.11], 
                                    [3,123.246,7.11]]
       },
       {
         "range": [[7.37, 7.54]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '104',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
	   {
         "range": [[7.60, 7.80]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64beta",
             "hkl": '310',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
	]

# output settings
Output_directory   = './'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360