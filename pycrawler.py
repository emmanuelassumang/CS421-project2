import os
import glob
import nltk
import string
from nltk.tokenize import word_tokenize


# base directory where the repositories are stored
base_dir = os.path.join(os.getcwd(), "repos")

# the output file
output_file = os.path.join(os.getcwd(), "python_filesmine.txt")

# output file in write mode
with open(output_file, 'w') as outfile:
    # Walk through each directory in the base directory
    for dir_name, _, _ in os.walk(base_dir):
        for py_file in glob.glob(os.path.join(dir_name, "*.py")):
            # Open each Python file in read mode
            with open(py_file, 'r') as infile:
                try:
                    # Read the file content
                    file_content = infile.read()

                    # Write the file content to the output file
                    outfile.write(f'====={py_file}=====\n{file_content}\n\n')
                except Exception as e:
                    print(f'Could not read file {py_file} due to {str(e)}')

