import sys
print(sys.executable)
print(sys.version_info)
sys.path.append("../../continuous-peak-fit/Continuous-Peak-Fit")
import cpf

for number in range(61,91):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022_additional/texture-studies/112748/sample_{number_string}/"
	input_filename = "INPUT_Diamond-2022_Ti64_22alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)

for number in range(91,94):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022_additional/texture-studies/112749/sample_{number_string}/"
	input_filename = "INPUT_Diamond-2022_Ti64_22alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)

for number in range(31,61):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022_additional/texture-studies/112750/sample_{number_string}/"
	input_filename = "INPUT_Diamond-2022_Ti64_22alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)

for number in range(1,31):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022_additional/texture-studies/114287/sample_{number_string}/"
	input_filename = "INPUT_Diamond-2022_Ti64_22alpha_4beta.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)