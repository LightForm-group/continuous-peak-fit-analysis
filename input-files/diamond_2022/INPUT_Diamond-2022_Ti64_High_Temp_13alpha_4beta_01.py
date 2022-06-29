# Input parameters for Ti64

# data drive.
import os 
drive = "/mnt/iusers01/jf01/mbcx9cd4/rds_lightform/"

# properties of the data files.
datafile_directory = drive + 'SXRD_raw_data/diamond_2022/rawdata/004_Ti64_TIFUN-R2_RD_Deform_850C_1mms-1_27_05_2022-004711'
datafile_Basename  = "pilatus_"
datafile_Ending    = ".cbf"
datafile_StartNum  = 1
datafile_EndNum    = 950
datafile_Step = 50
datafile_NumDigit  = 5

# calibration and masking.
Calib_type   = "Dioptas"
# Calib_detector = 'unknown'
# Calib_data     = drive + 'SXRD_analysis/desy_2021/calibration-dioptas/LaB6_1554mm_Dilatometer-00003.tif'
Calib_param    = drive + 'SXRD_analysis/diamond_2022/calibration-dioptas/CeO2_Diamond_2022_750mm.poni'
Calib_mask     = drive + 'SXRD_analysis/diamond_2022/calibration-dioptas/CeO2_Diamond_2022_750mm.mask'
Calib_pixels = 200


# number of bins for initial fitting.
AziBins = 90


# fitting properties for peaks.
fit_orders = [
       {
         "range": [[3.00, 3.20]],
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
         "range": [[3.20, 3.70]],
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
          "PeakPositionSelection": [[1,-120.5,3.36],
                                    [1,-58.997,3.36],
                                    [1,59.289,3.36],
                                    [1,23.187,3.36],
                                    [1,23.212,3.36], 
                                    [1,23.158,3.36], 
                                    [1,123.246,3.36],
                                    [2,-120.5,3.42],
                                    [2,-58.997,3.42],
                                    [2,59.289,3.42],
                                    [2,23.187,3.42],
                                    [2,23.212,3.42], 
                                    [2,23.158,3.42], 
                                    [2,123.246,3.42],
                                    [3,-120.5,3.53],
                                    [3,-58.997,3.53],
                                    [3,59.289,3.53],
                                    [3,23.187,3.53],
                                    [3,23.212,3.53], 
                                    [3,23.158,3.53], 
                                    [3,123.246,3.53]]
       },
       {
         "range": [[4.40, 4.72]],
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
         "range": [[4.72, 4.97]],
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
         "range": [[5.25, 5.51]],
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
         "range": [[5.80, 6.04]],
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
         "range": [[6.03, 6.60]],
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
          "PeakPositionSelection": [[1,-120.5,6.21],
                                    [1,-58.997,6.21],
                                    [1,59.289,6.21],
                                    [1,23.187,6.21],
                                    [1,23.212,6.21], 
                                    [1,23.158,6.21], 
                                    [1,123.246,6.21],
                                    [2,-120.5,6.34],
                                    [2,-58.997,6.34],
                                    [2,59.289,6.34],
                                    [2,23.187,6.34],
                                    [2,23.212,6.34], 
                                    [2,23.158,6.34], 
                                    [2,123.246,6.34],
                                    [3,-120.5,6.43],
                                    [3,-58.997,6.43],
                                    [3,59.289,6.43],
                                    [3,23.187,6.43],
                                    [3,23.212,6.43], 
                                    [3,23.158,6.43], 
                                    [3,123.246,6.43]]
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
          "PeakPositionSelection": [[1,-120.5,6.72],
                                    [1,-58.997,6.72],
                                    [1,59.289,6.72],
                                    [1,23.187,6.72],
                                    [1,23.212,6.72], 
                                    [1,23.158,6.72], 
                                    [1,123.246,6.72],
                                    [2,-120.5,6.85],
                                    [2,-58.997,6.85],
                                    [2,59.289,6.85],
                                    [2,23.187,6.85],
                                    [2,23.212,6.85], 
                                    [2,23.158,6.85], 
                                    [2,123.246,6.85],
                                    [3,-120.5,7.06],
                                    [3,-58.997,7.06],
                                    [3,59.289,7.06],
                                    [3,23.187,7.06],
                                    [3,23.212,7.06], 
                                    [3,23.158,7.06], 
                                    [3,123.246,7.06]]
       },
       {
         "range": [[7.26, 7.55]],
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
         "range": [[7.52, 7.80]],
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
       {
         "range": [[7.85, 8.16]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '203',
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
Output_directory   = drive + 'SXRD_analysis/diamond_2022/004_Ti64_TIFUN-R2_RD_Deform_850C_1mms-1/fourier-peak-analysis/'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360