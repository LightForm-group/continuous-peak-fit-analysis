# Input parameters for Ti64

# data drive.
import os 
drive = "D:/Chris Daniel/"

# properties of the data files.
datafile_directory = drive + 'continuous-peak-fit-analysis/example-data/Diamond_2021'
datafile_Basename  = "103818_summed_"
datafile_Ending    = ".tiff"
datafile_StartNum  = 1
datafile_EndNum    = 1
datafile_NumDigit  = 5

# calibration and masking.
Calib_type   = "Dioptas"
Calib_detector = 'unknown'
Calib_data     = drive + 'continuous-peak-fit-analysis/example-calibration/Diamond_2021/103852-pilatus2M-files/00001.cbf'
Calib_param    = 'example-calibration/Diamond_2021/103852-pilatus2M-files/calibration_103852.poni'
Calib_mask     = 'example-calibration/Diamond_2021/103852-pilatus2M-files/mask_103852.mask'
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
                                    [2,-120.5,3.20],
                                    [2,-58.997,3.20],
                                    [2,59.289,3.20],
                                    [2,23.187,3.20],
                                    [2,23.212,3.20], 
                                    [2,23.158,3.20], 
                                    [2,123.246,3.20]]
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
          "PeakPositionSelection": [[1,-120.5,5.60],
                                    [1,-58.997,5.60],
                                    [1,59.289,5.60],
                                    [1,23.187,5.60],
                                    [1,23.212,5.60], 
                                    [1,23.158,5.60], 
                                    [1,123.246,5.60],
                                    [2,-120.5,5.75],
                                    [2,-58.997,5.75],
                                    [2,59.289,5.75],
                                    [2,23.187,5.75],
                                    [2,23.212,5.75], 
                                    [2,23.158,5.75], 
                                    [2,123.246,5.75],
                                    [3,-120.5,5.82],
                                    [3,-58.997,5.82],
                                    [3,59.289,5.82],
                                    [3,23.187,5.82],
                                    [3,23.212,5.82], 
                                    [3,23.158,5.82], 
                                    [3,123.246,5.82]]
       },
	   {
         "range": [[5.97, 6.25]],
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
           }],
       },
	          {
         "range": [[6.23, 6.57]],
         "background": [0,0],
         "peak": [{
             "phase": "Ti64alpha",
             "hkl": '202',
             "d-space": 2,
             "height": 6,
             "profile": 0,
             #"profile_fixed": 1,
             "width": 0,
             "symmetry": 2
           }],
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
         "range": [[7.00, 7.94]],
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
                                    [2,-120.5,7.46],
                                    [2,-58.997,7.46],
                                    [2,59.289,7.46],
                                    [2,23.187,7.46],
                                    [2,23.212,7.46], 
                                    [2,23.158,7.46], 
                                    [2,123.246,7.46],
                                    [3,-120.5,7.59],
                                    [3,-58.997,7.59],
                                    [3,59.289,7.59],
                                    [3,23.187,7.59],
                                    [3,23.212,7.59], 
                                    [3,23.158,7.59], 
                                    [3,123.246,7.59],
									[4,-120.5,7.80],
                                    [4,-58.997,7.80],
                                    [4,59.289,7.80],
                                    [4,23.187,7.80],
                                    [4,23.212,7.80], 
                                    [4,23.158,7.80], 
                                    [4,123.246,7.80]]
       },
	   {
         "range": [[7.91, 8.58]],
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
          "PeakPositionSelection": [[1,-120.5,8.03],
                                    [1,-58.997,8.03],
                                    [1,59.289,8.03],
                                    [1,23.187,8.03],
                                    [1,23.212,8.03], 
                                    [1,23.158,8.03], 
                                    [1,123.246,8.03],
                                    [2,-120.5,8.13],
                                    [2,-58.997,8.13],
                                    [2,59.289,8.13],
                                    [2,23.187,8.13],
                                    [2,23.212,8.13], 
                                    [2,23.158,8.13], 
                                    [2,123.246,8.13],
                                    [3,-120.5,8.29],
                                    [3,-58.997,8.29],
                                    [3,59.289,8.29],
                                    [3,23.187,8.29],
                                    [3,23.212,8.29], 
                                    [3,23.158,8.29], 
                                    [3,123.246,8.29],
									[4,-120.5,8.41],
                                    [4,-58.997,8.41],
                                    [4,59.289,8.41],
                                    [4,23.187,8.41],
                                    [4,23.212,8.41], 
                                    [4,23.158,8.41], 
                                    [4,123.246,8.41]]
       },  
	   {
         "range": [[8.57, 8.86]],
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
Output_directory   = './'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360