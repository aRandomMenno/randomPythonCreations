
import hashlib

input_file_path = "put path to file here" # ! important: use double backslashes if using absolute path!
output_file_path = "./output.txt"

seen_lines = set()

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        hash_value = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hash_value not in seen_lines:
            output_file.write(line)
            seen_lines.add(hash_value)

print("Finished.")