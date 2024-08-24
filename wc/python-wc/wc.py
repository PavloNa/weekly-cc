#Imports
import sys, os, locale

# Data
argv = sys.argv[1:]
locale.setlocale(locale.LC_ALL, 'en_US.utf8')

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

def character_return(lines):
    #This runs for the -m
    char_count = 0
    for line in lines:
        char_count += len(line)
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
    
    if len(argv) == 2:
        arg_type = argv[0]
        file_name = argv[1]
        
        try:
            with open(file_name) as file:
                contents = file.read()
                lines = file.readlines()
                if arg_type == "-c":
                    print(f"{byte_return(file_name)} {file_name}")
                if arg_type == "-l":
                    print(f"{line_return(lines)} {file_name}")
                if arg_type == "-w":
                    print(f"{word_return(lines)} {file_name}")
                if arg_type == "-m":
                    print(f"{character_return(contents)} {file_name}")
        except Exception as e:
            print("Wrong use of arguments or file")
            print("For more information run: python3 wc.py -h")
            print(f"Exception: {e}")

# Run
if __name__ == "__main__":
    main()