# This Python script prints out the header and sequence of the Uniprot number you are looking for in the .fasta file.
# The only thing you have to do is replace the fasta file path with your own, and the system will remind you to enter the Uniprot number. 

def print_fasta(fasta_file, target_uniprot):
    """
    Prints the header and sequence for the specified UniProt ID from a FASTA file.

    Parameters:
        fasta_file (str): Path to the FASTA file.
        target_uniprot (str): UniProt ID to search for.
    """
    with open(fasta_file, 'r') as file:
        print_sequence = False
        header = ""
        sequence = ""

        for line in file:
            if line.startswith('>'):
                if target_uniprot in line:
                    print_sequence = True
                    header = line.strip()  # Save the header line
                    sequence = ""  # Reset sequence for the target UniProt ID
                else:
                    print_sequence = False
            elif print_sequence:
                sequence += line.strip()  # Collect sequence line by line

        # Print the header and sequence together if the target was found
        if header and sequence:
            print(header)
            print(sequence)
        else:
            print(f"No sequence found for UniProt ID: {target_uniprot}!")

# Specify the path to your FASTA file
fasta_file_path = "./3000-4000_onefasta.fasta" # Replace with the path of your .fasta file
target_uniprot_number = input("Type your UniProt number here: ")

print_fasta(fasta_file_path, target_uniprot_number)
