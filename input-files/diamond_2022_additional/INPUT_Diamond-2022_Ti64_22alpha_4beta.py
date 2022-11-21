# Input parameters for Ti64

# data drive.
import os 
drive = "/mnt/iusers01/jf01/mbcx9cd4/rds_lightform/"

# properties of the data files.
datafile_directory = drive + 'SXRD_analysis/diamond_2022_additional/texture-studies/112748/sample_61'
datafile_Basename  = "112748_summed"
datafile_Ending    = ".tiff"
datafile_StartNum  = 1
datafile_EndNum    = 1
datafile_Step = 1
datafile_NumDigit  = 1

# calibration and masking.
Calib_type   = "Dioptas"
# Calib_detector = 'unknown'
# Calib_data     = drive + 'SXRD_analysis/diamond_2022/calibration-dioptas/00001.tif'
Calib_param    = drive + 'SXRD_analysis/diamond_2022_additional/calibration-dioptas/july/112747_LaB6_Diamond_2022_640mm.poni'
Calib_mask     = drive + 'SXRD_analysis/diamond_2022_additional/calibration-dioptas/july/112747_LaB6_Diamond_2022_640mm.mask'
Calib_pixels = 200


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
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[3.27, 3.73]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '002',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64beta",
             "hkl": '110',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '101',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,3.39],
                                    [1,-58.997,3.39],
                                    [1,59.289,3.39],
                                    [1,23.187,3.39],
                                    [1,23.212,3.39], 
                                    [1,23.158,3.39], 
                                    [1,123.246,3.39],
                                    [2,-120.5,3.47],
                                    [2,-58.997,3.47],
                                    [2,59.289,3.47],
                                    [2,23.187,3.47],
                                    [2,23.212,3.47], 
                                    [2,23.158,3.47], 
                                    [2,123.246,3.47],
                                    [3,-120.5,3.56],
                                    [3,-58.997,3.56],
                                    [3,59.289,3.56],
                                    [3,23.187,3.56],
                                    [3,23.212,3.56], 
                                    [3,23.158,3.56], 
                                    [3,123.246,3.56]]
       },
       {
         "range": [[4.45, 4.74]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '102',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[4.80, 5.05]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64beta",
             "hkl": '200',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[5.28, 5.59]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '110',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[5.85, 6.10]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '103',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
       {
         "range": [[6.14, 6.66]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '200',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '112',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '201',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,6.26],
                                    [1,-58.997,6.26],
                                    [1,59.289,6.26],
                                    [1,23.187,6.26],
                                    [1,23.212,6.26], 
                                    [1,23.158,6.26], 
                                    [1,123.246,6.26],
                                    [2,-120.5,6.39],
                                    [2,-58.997,6.39],
                                    [2,59.289,6.39],
                                    [2,23.187,6.39],
                                    [2,23.212,6.39], 
                                    [2,23.158,6.39], 
                                    [2,123.246,6.39],
                                    [3,-120.5,6.48],
                                    [3,-58.997,6.48],
                                    [3,59.289,6.48],
                                    [3,23.187,6.48],
                                    [3,23.212,6.48], 
                                    [3,23.158,6.48], 
                                    [3,123.246,6.48]]
       },
       {
         "range": [[6.64, 7.29]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '004',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64beta",
             "hkl": '220',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           },{
             "phase": "Ti64alpha",
             "hkl": '202',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
          "PeakPositionSelection": [[1,-120.5,6.78],
                                    [1,-58.997,6.78],
                                    [1,59.289,6.78],
                                    [1,23.187,6.78],
                                    [1,23.212,6.78], 
                                    [1,23.158,6.78], 
                                    [1,123.246,6.78],
                                    [2,-120.5,6.94],
                                    [2,-58.997,6.94],
                                    [2,59.289,6.94],
                                    [2,23.187,6.94],
                                    [2,23.212,6.94], 
                                    [2,23.158,6.94], 
                                    [2,123.246,6.94],
                                    [3,-120.5,7.11],
                                    [3,-58.997,7.11],
                                    [3,59.289,7.11],
                                    [3,23.187,7.11],
                                    [3,23.212,7.11], 
                                    [3,23.158,7.11], 
                                    [3,123.246,7.11]]
       },
       {
         "range": [[7.30, 7.62]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '104',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
	   {
         "range": [[7.60, 7.90]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64beta",
             "hkl": '310',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
	   {
         "range": [[7.90, 8.82]],
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
          "PeakPositionSelection": [[1,-120.5,8.06],
                                    [1,-58.997,8.06],
                                    [1,59.289,8.06],
                                    [1,23.187,8.06],
                                    [1,23.212,8.06], 
                                    [1,23.158,8.06], 
                                    [1,123.246,8.06],
                                    [2,-120.5,8.27],
                                    [2,-58.997,8.27],
                                    [2,59.289,8.27],
                                    [2,23.187,8.27],
                                    [2,23.212,8.27], 
                                    [2,23.158,8.27], 
                                    [2,123.246,8.27],
                                    [3,-120.5,8.44],
                                    [3,-58.997,8.44],
                                    [3,59.289,8.44],
                                    [3,23.187,8.44],
                                    [3,23.212,8.44], 
                                    [3,23.158,8.44], 
                                    [3,123.246,8.44],
									[4,-120.5,8.67],
                                    [4,-58.997,8.67],
                                    [4,59.289,8.67],
                                    [4,23.187,8.67],
                                    [4,23.212,8.67], 
                                    [4,23.158,8.67], 
                                    [4,123.246,8.67]]
       },
	   {
         "range": [[8.82, 9.55]],
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
          "PeakPositionSelection": [[1,-120.5,8.94],
                                    [1,-58.997,8.94],
                                    [1,59.289,8.94],
                                    [1,23.187,8.94],
                                    [1,23.212,8.94], 
                                    [1,23.158,8.94], 
                                    [1,123.246,8.94],
                                    [2,-120.5,9.04],
                                    [2,-58.997,9.04],
                                    [2,59.289,9.04],
                                    [2,23.187,9.04],
                                    [2,23.212,9.04], 
                                    [2,23.158,9.04], 
                                    [2,123.246,9.04],
                                    [3,-120.5,9.22],
                                    [3,-58.997,9.22],
                                    [3,59.289,9.22],
                                    [3,23.187,9.22],
                                    [3,23.212,9.22], 
                                    [3,23.158,9.22], 
                                    [3,123.246,9.22],
									[4,-120.5,9.38],
                                    [4,-58.997,9.38],
                                    [4,59.289,9.38],
                                    [4,23.187,9.38],
                                    [4,23.212,9.38], 
                                    [4,23.158,9.38], 
                                    [4,123.246,9.38]]
       },
       {
         "range": [[9.56, 9.85]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '301',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
	   {
         "range": [[9.85, 10.10]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '213',
             "d-space": 2,
             "height": 6,
             "height-type": "spline-cubic",
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
       },
	]

# output settings
Output_directory   = drive + 'SXRD_analysis/diamond_2022_additional/texture-studies/112748/sample_61'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360