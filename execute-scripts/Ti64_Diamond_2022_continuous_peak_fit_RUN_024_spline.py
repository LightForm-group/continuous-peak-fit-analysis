import sys
print(sys.executable)
print(sys.version_info)
sys.path.append("../../continuous-peak-fit/Continuous-Peak-Fit")
import cpf
input_filepath = "../../../SXRD_analysis/diamond_2022/024_Ti64_Sheet_45deg_RT-Deform_1Ns-1/fourier-peak-analysis/"
input_filename = "INPUT_Diamond-2022_Ti64_13alpha_4beta_01.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.initiate(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)