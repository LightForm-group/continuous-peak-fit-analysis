import sys
print(sys.executable)
print(sys.version_info)
sys.path.append("../../continuous-peak-fit/Continuous-Peak-Fit")
import cpf
input_filepath = "../example-input-files/"
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_1.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.initiate(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_2.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_3.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_4.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_5.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_6.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_7.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_8.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)
input_filename = "EXAMPLE_INPUT_Diamond-2021_Ti64_21alpha_4beta_iCSF_9.py"
input_file = f"{input_filepath}{input_filename}"
print(input_file)
cpf.XRD_FitPattern.execute(input_file)
# cpf.XRD_FitPattern.write_output(input_file)