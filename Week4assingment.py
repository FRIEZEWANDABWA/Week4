def read_and_modify_file():
    # Ask user for input filename
    input_file = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (example: converting text to uppercase)
        modified_content = content.upper()

        # Create a new file to write the modified content
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: Could not read from or write to '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
