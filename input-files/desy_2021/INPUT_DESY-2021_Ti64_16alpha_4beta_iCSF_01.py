# Input parameters for Ti64

# data drive.
import os 
drive = "/mnt/iusers01/jf01/mbcx9cd4/rds_lightform/"

# properties of the data files.
datafile_directory = drive + 'SXRD_raw_data/desy_2021/diffraction_images/Def_04'
datafile_Basename  = "Ti64_Rolled_ND_Compress_910C_1-00s-1_Multi-Hit_Temp_Cycl_4Cs-1_810_Cool_4Cs-1_Def04_1-"
datafile_Ending    = ".tif"
datafile_StartNum  = 1
datafile_EndNum    = 1900
datafile_Step = 50
datafile_NumDigit  = 5

# calibration and masking.
Calib_type   = "Dioptas"
# Calib_detector = 'unknown'
# Calib_data     = drive + 'SXRD_analysis/desy_2021/calibration-dioptas/LaB6_1554mm_Dilatometer-00003.tif'
Calib_param    = drive + 'SXRD_analysis/desy_2021/calibration-dioptas/LaB6_1554mm_Dilatometer-00003.poni'
Calib_mask     = drive + 'SXRD_analysis/desy_2021/calibration-dioptas/LaB6_1554mm_Dilatometer-00003.mask'
Calib_pixels = 200


# number of bins for initial fitting.
AziBins = 90


# fitting properties for peaks.
fit_orders = [
       {
         "range": [[2.66, 2.91]],
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
         "range": [[2.91, 3.34]],
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
                                    [2,-120.5,3.11],
                                    [2,-58.997,3.11],
                                    [2,59.289,3.11],
                                    [2,23.187,3.11],
                                    [2,23.212,3.11], 
                                    [2,23.158,3.11], 
                                    [2,123.246,3.11],
                                    [3,-120.5,3.19],
                                    [3,-58.997,3.19],
                                    [3,59.289,3.19],
                                    [3,23.187,3.19],
                                    [3,23.212,3.19], 
                                    [3,23.158,3.19], 
                                    [3,123.246,3.19]]
       },
       {
         "range": [[3.99, 4.24]],
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
         "range": [[4.23, 4.52]],
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
         "range": [[4.70, 5.01]],
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
         "range": [[5.15, 5.52]],
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
         "range": [[5.46, 5.94]],
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
          "PeakPositionSelection": [[1,-120.5,5.61],
                                    [1,-58.997,5.61],
                                    [1,59.289,5.61],
                                    [1,23.187,5.61],
                                    [1,23.212,5.61], 
                                    [1,23.158,5.61], 
                                    [1,123.246,5.61],
                                    [2,-120.5,5.73],
                                    [2,-58.997,5.73],
                                    [2,59.289,5.73],
                                    [2,23.187,5.73],
                                    [2,23.212,5.73], 
                                    [2,23.158,5.73], 
                                    [2,123.246,5.73],
                                    [3,-120.5,5.82],
                                    [3,-58.997,5.82],
                                    [3,59.289,5.82],
                                    [3,23.187,5.82],
                                    [3,23.212,5.82], 
                                    [3,23.158,5.82], 
                                    [3,123.246,5.82]]
       },
       {
         "range": [[5.93, 6.49]],
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
          "PeakPositionSelection": [[1,-120.5,6.08],
                                    [1,-58.997,6.08],
                                    [1,59.289,6.08],
                                    [1,23.187,6.08],
                                    [1,23.212,6.08], 
                                    [1,23.158,6.08], 
                                    [1,123.246,6.08],
                                    [2,-120.5,6.23],
                                    [2,-58.997,6.23],
                                    [2,59.289,6.23],
                                    [2,23.187,6.23],
                                    [2,23.212,6.23], 
                                    [2,23.158,6.23], 
                                    [2,123.246,6.23],
                                    [3,-120.5,6.38],
                                    [3,-58.997,6.38],
                                    [3,59.289,6.38],
                                    [3,23.187,6.38],
                                    [3,23.212,6.38], 
                                    [3,23.158,6.38], 
                                    [3,123.246,6.38]]
       },
       {
         "range": [[6.53, 6.78]],
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
         "range": [[6.77, 7.09]],
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
         "range": [[7.07, 7.90]],
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
          "PeakPositionSelection": [[1,-120.5,7.23],
                                    [1,-58.997,7.23],
                                    [1,59.289,7.23],
                                    [1,23.187,7.23],
                                    [1,23.212,7.23], 
                                    [1,23.158,7.23], 
                                    [1,123.246,7.23],
                                    [2,-120.5,7.42],
                                    [2,-58.997,7.42],
                                    [2,59.289,7.42],
                                    [2,23.187,7.42],
                                    [2,23.212,7.42], 
                                    [2,23.158,7.42], 
                                    [2,123.246,7.42],
                                    [3,-120.5,7.58],
                                    [3,-58.997,7.58],
                                    [3,59.289,7.58],
                                    [3,23.187,7.58],
                                    [3,23.212,7.58], 
                                    [3,23.158,7.58], 
                                    [3,123.246,7.58],
									[4,-120.5,7.79],
                                    [4,-58.997,7.79],
                                    [4,59.289,7.79],
                                    [4,23.187,7.79],
                                    [4,23.212,7.79], 
                                    [4,23.158,7.79], 
                                    [4,123.246,7.79]]
       },  
	]

# output settings
Output_directory   = drive + 'SXRD_analysis/desy_2021/experiment04-deformation/fourier-peak-analysis/'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360