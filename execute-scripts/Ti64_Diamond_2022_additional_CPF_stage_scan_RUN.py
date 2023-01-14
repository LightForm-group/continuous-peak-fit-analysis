import sys
print(sys.executable)
print(sys.version_info)
sys.path.append("../../continuous-peak-fit/Continuous-Peak-Fit")
import cpf

for number in range(1,10):
	number_string = str(number)
	input_filepath = f"../../../SXRD_analysis/diamond_2022_additional/texture-studies/112750-stage-scan/sample_4/"
	input_filename = f"INPUT_Diamond-2022_Ti64_22alpha_4beta_line{number_string}.py"
	input_file = f"{input_filepath}{input_filename}"
	print(input_file)
	cpf.XRD_FitPattern.initiate(input_file)
	cpf.XRD_FitPattern.execute(input_file)
	# cpf.XRD_FitPattern.write_output(input_file)