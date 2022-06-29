import sys
print(sys.executable)
print(sys.version_info)
sys.path.append("../../continuous-peak-fit/Continuous-Peak-Fit")
import cpf

for number in range(111439,111469):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022/texture-studies/{number_string}/fourier-peak-analysis/"
	input_filename = "INPUT_Diamond-2022_Ti64_13alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)

for number in range(111575,111577):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022/texture-studies/{number_string}/fourier-peak-analysis/"
	input_filename = "INPUT_Diamond-2022_Ti64_13alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)

for number in range(111578,111605):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022/texture-studies/{number_string}/fourier-peak-analysis/"
	input_filename = "INPUT_Diamond-2022_Ti64_13alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)

for number in range(111606,111607):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022/texture-studies/{number_string}/fourier-peak-analysis/"
	input_filename = "INPUT_Diamond-2022_Ti64_13alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)