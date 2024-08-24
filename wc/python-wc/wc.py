#Imports
import sys
import os

# Data
argv = sys.argv[1:]

# Functions
def error_handling():
    if not argv:
        print("Usage: python3 wc.py <filename>")
        print("For more information run: python3 wc.py -h")
        exit()
    if len(argv) > 2:
        print("Usage: python3 wc.py <filename>")
        print("For more information run: python3 wc.py -h")
        exit()

def byte_return(file):
    #This runs for the -c
    file_size = os.path.getsize(file)
    return file_size

def line_return(lines):
    #This runs for the -l
    line_count = len(lines)
    return line_count

def word_return(lines):
    #This runs for the -w
    word_count = sum(len(line.split()) for line in lines)
    return word_count

def character_return(file):
    #This runs for the -m
    contents = file.read()
    char_count = len(contents)
    return char_count


# Main function
def main():
    error_handling()
    if len(argv) == 1:
        file_name = argv[0]
        if file_name == "-h":
            print("help template")
            exit()
        with open(file_name) as file:
            lines = file.readlines()
            print(f"  {line_return(lines)}  {word_return(lines)} {byte_return(file_name)} {file_name}")

# Run
if __name__ == "__main__":
    main()