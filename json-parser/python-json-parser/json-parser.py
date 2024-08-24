#Imports
import sys

# Data
argv = sys.argv[1:]

# Functions
def error_checker(file):
    if not file.read():
        print("File is empty and not a valid JSON.")

#Main
def main():
    try:
        with open(argv[0]) as file:
            error_checker(file)
            print("JSON file is valid.")
            
    except:
        print("An error occured.")

# Run
if __name__ == "__main__":
    main()