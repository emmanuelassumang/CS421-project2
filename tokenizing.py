import os
from gensim.utils import simple_preprocess

# Initialize an empty list to store the tokenized lines
code = []

# Define the output file path
output_file = os.path.join(os.getcwd(), "python_filesmine.txt")

# Open the output file in read mode
with open(output_file, 'r') as f:
    # Read the entire content of the file into a string
    corpus = f.read()
    
    # Split the string into lines
    raw_lines = corpus.splitlines()
    
    for line in raw_lines:
        code.append(simple_preprocess(line))

# Print the number of lines of code, which is the length of the 'code' list
print(f'Number of lines of code: {len(code)}')

# Print the number of tokens, which is the sum of the lengths of the lists in the 'code' list
print(f'Number of tokens (words): {len([token for sent in code for token in sent])}')
