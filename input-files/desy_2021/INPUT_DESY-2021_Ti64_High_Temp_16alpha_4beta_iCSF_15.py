# Input parameters for Ti64

# data drive.
import os 
drive = "/mnt/iusers01/jf01/mbcx9cd4/rds_lightform/"

# properties of the data files.
datafile_directory = drive + 'SXRD_raw_data/desy_2021/diffraction_images/Def_04'
datafile_Basename  = "Ti64_Rolled_ND_Compress_910C_1-00s-1_Multi-Hit_Temp_Cycl_4Cs-1_810_Cool_4Cs-1_Def04_5-"
datafile_Ending    = ".tif"
datafile_StartNum  = 300
datafile_EndNum    = 2229
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
          "PeakPositionSelection": [[1,-120.5,3.01],
                                    [1,-58.997,3.01],
                                    [1,59.289,3.01],
                                    [1,23.187,3.01],
                                    [1,23.212,3.01], 
                                    [1,23.158,3.01], 
                                    [1,123.246,3.01],
                                    [2,-120.5,3.06],
                                    [2,-58.997,3.06],
                                    [2,59.289,3.06],
                                    [2,23.187,3.06],
                                    [2,23.212,3.06], 
                                    [2,23.158,3.06], 
                                    [2,123.246,3.06],
                                    [3,-120.5,3.16],
                                    [3,-58.997,3.16],
                                    [3,59.289,3.16],
                                    [3,23.187,3.16],
                                    [3,23.212,3.16], 
                                    [3,23.158,3.16], 
                                    [3,123.246,3.16]]
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
          "PeakPositionSelection": [[1,-120.5,5.56],
                                    [1,-58.997,5.56],
                                    [1,59.289,5.56],
                                    [1,23.187,5.56],
                                    [1,23.212,5.56], 
                                    [1,23.158,5.56], 
                                    [1,123.246,5.56],
                                    [2,-120.5,5.68],
                                    [2,-58.997,5.68],
                                    [2,59.289,5.68],
                                    [2,23.187,5.68],
                                    [2,23.212,5.68], 
                                    [2,23.158,5.68], 
                                    [2,123.246,5.68],
                                    [3,-120.5,5.76],
                                    [3,-58.997,5.76],
                                    [3,59.289,5.76],
                                    [3,23.187,5.76],
                                    [3,23.212,5.76], 
                                    [3,23.158,5.76], 
                                    [3,123.246,5.76]]
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
          "PeakPositionSelection": [[1,-120.5,6.02],
                                    [1,-58.997,6.02],
                                    [1,59.289,6.02],
                                    [1,23.187,6.02],
                                    [1,23.212,6.02], 
                                    [1,23.158,6.02], 
                                    [1,123.246,6.02],
                                    [2,-120.5,6.12],
                                    [2,-58.997,6.12],
                                    [2,59.289,6.12],
                                    [2,23.187,6.12],
                                    [2,23.212,6.12], 
                                    [2,23.158,6.12], 
                                    [2,123.246,6.12],
                                    [3,-120.5,6.32],
                                    [3,-58.997,6.32],
                                    [3,59.289,6.32],
                                    [3,23.187,6.32],
                                    [3,23.212,6.32], 
                                    [3,23.158,6.32], 
                                    [3,123.246,6.32]]
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
          "PeakPositionSelection": [[1,-120.5,7.16],
                                    [1,-58.997,7.16],
                                    [1,59.289,7.16],
                                    [1,23.187,7.16],
                                    [1,23.212,7.16], 
                                    [1,23.158,7.16], 
                                    [1,123.246,7.16],
                                    [2,-120.5,7.36],
                                    [2,-58.997,7.36],
                                    [2,59.289,7.36],
                                    [2,23.187,7.36],
                                    [2,23.212,7.36], 
                                    [2,23.158,7.36], 
                                    [2,123.246,7.36],
                                    [3,-120.5,7.50],
                                    [3,-58.997,7.50],
                                    [3,59.289,7.50],
                                    [3,23.187,7.50],
                                    [3,23.212,7.50], 
                                    [3,23.158,7.50], 
                                    [3,123.246,7.50],
									[4,-120.5,7.71],
                                    [4,-58.997,7.71],
                                    [4,59.289,7.71],
                                    [4,23.187,7.71],
                                    [4,23.212,7.71], 
                                    [4,23.158,7.71], 
                                    [4,123.246,7.71]]
       },  
	]

# output settings
Output_directory   = drive + 'SXRD_analysis/desy_2021/experiment04-deformation/fourier-peak-analysis/'
Output_type        = 'MultiFit' #'DifferentialStrain' # differential strain option gives the principal stress/strain axis
Output_NumAziWrite = 360