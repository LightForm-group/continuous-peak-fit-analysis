# Input parameters for Ti64

# data drive.
import os 
drive = "/mnt/iusers01/jf01/mbcx9cd4/rds_lightform/"

# properties of the data files.
datafile_directory = drive + 'SXRD_raw_data/diamond_2021/rawdata/103845-pilatus2M-files'
datafile_Basename  = "00"
datafile_Ending    = ".cbf"
datafile_StartNum  = 260
datafile_EndNum    = 300
datafile_NumDigit  = 3

# calibration and masking.
Calib_type   = "Dioptas"
# Calib_detector = 'unknown'
# Calib_data     = drive + 'SXRD_analysis/diamond_2021/103852-calibration/00001.cbf'
Calib_param    = drive + 'SXRD_analysis/diamond_2021/103852-calibration/calibration_103852.poni'
Calib_mask     = drive + 'SXRD_analysis/diamond_2021/103852-calibration/mask_103852.mask'
Calib_pixels = 172


# number of bins for initial fitting.
AziBins = 90


# fitting properties for peaks.
fit_orders = [
       {
         "range": [[2.70, 2.93]],
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
         "range": [[2.93, 3.36]],
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
          "PeakPositionSelection": [[1,-120.5,3.04],
                                    [1,-58.997,3.04],
                                    [1,59.289,3.04],
                                    [1,23.187,3.04],
                                    [1,23.212,3.04], 
                                    [1,23.158,3.04], 
                                    [1,123.246,3.04],
                                    [2,-120.5,3.12],
                                    [2,-58.997,3.12],
                                    [2,59.289,3.12],
                                    [2,23.187,3.12],
                                    [2,23.212,3.12], 
                                    [2,23.158,3.12], 
                                    [2,123.246,3.12],
                                    [3,-120.5,3.20],
                                    [3,-58.997,3.20],
                                    [3,59.289,3.20],
                                    [3,23.187,3.20],
                                    [3,23.212,3.20], 
                                    [3,23.158,3.20], 
                                    [3,123.246,3.20]]
       },
       {
         "range": [[4.05, 4.25]],
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
         "range": [[4.30, 4.56]],
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
         "range": [[4.70, 5.02]],
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
         "range": [[5.20, 5.53]],
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
         "range": [[5.53, 5.97]],
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
          "PeakPositionSelection": [[1,-120.5,5.62],
                                    [1,-58.997,5.62],
                                    [1,59.289,5.62],
                                    [1,23.187,5.62],
                                    [1,23.212,5.62], 
                                    [1,23.158,5.62], 
                                    [1,123.246,5.62],
                                    [2,-120.5,5.75],
                                    [2,-58.997,5.75],
                                    [2,59.289,5.75],
                                    [2,23.187,5.75],
                                    [2,23.212,5.75], 
                                    [2,23.158,5.75], 
                                    [2,123.246,5.75],
                                    [3,-120.5,5.83],
                                    [3,-58.997,5.83],
                                    [3,59.289,5.83],
                                    [3,23.187,5.83],
                                    [3,23.212,5.83], 
                                    [3,23.158,5.83], 
                                    [3,123.246,5.83]]
       },
       {
         "range": [[5.97, 6.57]],
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
          "PeakPositionSelection": [[1,-120.5,6.10],
                                    [1,-58.997,6.10],
                                    [1,59.289,6.10],
                                    [1,23.187,6.10],
                                    [1,23.212,6.10], 
                                    [1,23.158,6.10], 
                                    [1,123.246,6.10],
                                    [2,-120.5,6.24],
                                    [2,-58.997,6.24],
                                    [2,59.289,6.24],
                                    [2,23.187,6.24],
                                    [2,23.212,6.24], 
                                    [2,23.158,6.24], 
                                    [2,123.246,6.24],
                                    [3,-120.5,6.40],
                                    [3,-58.997,6.40],
                                    [3,59.289,6.40],
                                    [3,23.187,6.40],
                                    [3,23.212,6.40], 
                                    [3,23.158,6.40], 
                                    [3,123.246,6.40]]
       },
       {
         "range": [[6.55, 6.86]],
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
         "range": [[6.85, 7.15]],
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
         "range": [[7.13, 7.95]],
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
           },{
             "phase": "Ti64alpha",
             "hkl": '210',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '211',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
		   },{
             "phase": "Ti64alpha",
             "hkl": '114',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,7.25],
                                    [1,-58.997,7.25],
                                    [1,59.289,7.25],
                                    [1,23.187,7.25],
                                    [1,23.212,7.25], 
                                    [1,23.158,7.25], 
                                    [1,123.246,7.25],
                                    [2,-120.5,7.44],
                                    [2,-58.997,7.44],
                                    [2,59.289,7.44],
                                    [2,23.187,7.44],
                                    [2,23.212,7.44], 
                                    [2,23.158,7.44], 
                                    [2,123.246,7.44],
                                    [3,-120.5,7.60],
                                    [3,-58.997,7.60],
                                    [3,59.289,7.60],
                                    [3,23.187,7.60],
                                    [3,23.212,7.60], 
                                    [3,23.158,7.60], 
                                    [3,123.246,7.60],
									[4,-120.5,7.80],
                                    [4,-58.997,7.80],
                                    [4,59.289,7.80],
                                    [4,23.187,7.80],
                                    [4,23.212,7.80], 
                                    [4,23.158,7.80], 
                                    [4,123.246,7.80]]
       },
	   {
         "range": [[7.92, 8.59]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '212',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '105',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '204',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
		   },{
             "phase": "Ti64alpha",
             "hkl": '300',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,8.04],
                                    [1,-58.997,8.04],
                                    [1,59.289,8.04],
                                    [1,23.187,8.04],
                                    [1,23.212,8.04], 
                                    [1,23.158,8.04], 
                                    [1,123.246,8.04],
                                    [2,-120.5,8.13],
                                    [2,-58.997,8.13],
                                    [2,59.289,8.13],
                                    [2,23.187,8.13],
                                    [2,23.212,8.13], 
                                    [2,23.158,8.13], 
                                    [2,123.246,8.13],
                                    [3,-120.5,8.28],
                                    [3,-58.997,8.28],
                                    [3,59.289,8.28],
                                    [3,23.187,8.28],
                                    [3,23.212,8.28], 
                                    [3,23.158,8.28], 
                                    [3,123.246,8.28],
									[4,-120.5,8.44],
                                    [4,-58.997,8.44],
                                    [4,59.289,8.44],
                                    [4,23.187,8.44],
                                    [4,23.212,8.44], 
                                    [4,23.158,8.44], 
                                    [4,123.246,8.44]]
       },  
	   {
         "range": [[8.57, 8.88]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '301',
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
Output_directory   = drive + 'SXRD_analysis/diamond_2021/103845/texture-cpf-stage-scan/103845-cpf-output'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360