'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code


import json
from packaging import parse_packaging

def process_file(input_filename: str, output_filename: str):
    """
    Reads a file with package descriptions, parses them, and writes them to a JSON file.
    """
    parsed_packages = []

    with open(input_filename, "r") as file:
        for line in file:
            line = line.strip()  
            if line:  
                parsed_packages.append(parse_packaging(line))

    
    with open(output_filename, "w") as json_file:
        json.dump(parsed_packages, json_file, indent=4)

    print(f" Processed {len(parsed_packages)} packages. Output saved to {output_filename}")

if __name__ == "__main__":
   
    input_file = "packaging_data.txt"  
    output_file = "parsed_packages.json"
    process_file(input_file, output_file)
