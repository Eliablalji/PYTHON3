def process_file(input_filename, output_filename=None):
    """
    Reads a file, optionally modifies it (capitalizes), and writes to a new file or prints content.
    Handles file not found and permission errors.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()  # Read lines for potential modification

            if output_filename:  # If output file is specified, modify and write
                with open(output_filename, 'w') as outfile:
                    for line in content:
                        outfile.write(line.upper()) # Modify: capitalize each line
                print(f"File '{input_filename}' processed and saved to '{output_filename}' successfully.")
            else:  # If no output file, just print the contents
                print(f"Content of '{input_filename}':")
                for line in content:
                  print(line, end='') #print with no extra new lines

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{input_filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage:
# Create a sample input file if you don't have one:
# with open("my_input.txt", "w") as f:
#     f.write("This is a sample line.\nAnother line here.")

# To modify and save to a new file:
process_file("my_input.txt", "my_output.txt")

# To just read and print the content:
# process_file("my_input.txt")