def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Extract components and store them in a list
            components = [line.strip() for line in lines]

            return components

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
file_path = 'accessions.txt'  
result = read_txt_file(file_path)

if result:
    print(result)
