import sys
print(sys.executable)
print(sys.version_info)
sys.path.append("../../continuous-peak-fit/Continuous-Peak-Fit")
import cpf
# cpf.XRD_FitPattern.writeoutput(input_file)
input_filepath = "../../../SXRD_analysis/desy_2020/experiment09c-deformation/fourier-peak-analysis-correction/"
input_filename = "INPUT_DESY-2020_Ti64_High_Temp_14alpha_4beta_iCSF_02.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.initiate(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.writeoutput(input_file)
input_filepath = "../../../SXRD_analysis/desy_2020/experiment09c-deformation/fourier-peak-analysis-correction/"
input_filename = "INPUT_DESY-2020_Ti64_High_Temp_14alpha_4beta_iCSF_03.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.writeoutput(input_file)