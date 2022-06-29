import sys
print(sys.executable)
print(sys.version_info)
sys.path.append("../../continuous-peak-fit/Continuous-Peak-Fit")
import cpf
input_filepath = "../../../SXRD_analysis/diamond_2022/004_Ti64_TIFUN-R2_RD_Deform_850C_1mms-1/fourier-peak-analysis/"
input_filename = "INPUT_Diamond-2022_Ti64_High_Temp_13alpha_4beta_01.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.initiate(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filepath = "../../../SXRD_analysis/diamond_2022/004_Ti64_TIFUN-R2_RD_Deform_850C_1mms-1/fourier-peak-analysis/"
input_filename = "INPUT_Diamond-2022_Ti64_High_Temp_13alpha_4beta_02.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filepath = "../../../SXRD_analysis/diamond_2022/004_Ti64_TIFUN-R2_RD_Deform_850C_1mms-1/fourier-peak-analysis/"
input_filename = "INPUT_Diamond-2022_Ti64_High_Temp_13alpha_4beta_03.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)