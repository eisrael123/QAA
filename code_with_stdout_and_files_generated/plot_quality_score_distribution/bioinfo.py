#!/usr/bin/env python

# Author: ewi@uoregon.edu

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module
import os 

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.5"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning


DNA_bases = 'AGCT'
RNA_bases = 'AGCU'

def reverse_complement(sequence: str) -> str:
    '''Returns the reverse complement of a given DNA sequence'''
    assert (validate_base_seq(sequence)), "Not a DNA sequence."
    sequence = sequence.upper() 
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_seq = ''.join(complement_dict.get(base,'?') for base in sequence)
    reverse_complement = complement_seq[::-1]
    return reverse_complement

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score.'''
    return ord(letter) - 33

def qual_score(phred_score: str) -> float:
    '''Returns the average quality score of a given sequence.'''
    assert len(phred_score) != 0, "Sequence cannot be empty"
    total_phred_score = 0
    for char in phred_score:
        total_phred_score += convert_phred(char)
    return total_phred_score / len(phred_score)

def validate_base_seq(DNA: str, RNAflag: bool=False) -> bool:
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs, or Ns (false reads). False otherwise. Case insenstitive.'''
    DNA = DNA.upper()
    return (DNA.count('N') + DNA.count('A') + DNA.count('G') + DNA.count('C') + DNA.count('U' if RNAflag else 'T')) == len(DNA)

def gc_content(DNA: str) -> float:
    '''Returns GC content of a DNA or RNA sequence as a decimal between 0 and 1.'''
    if 'T' in DNA:
        assert (validate_base_seq(DNA)), "Not a DNA sequence."
    else:
        assert (validate_base_seq(DNA,True)), "Not a RNA sequence." 
    if len(DNA) == 0:
        return 0 
    return (DNA.count('G') + DNA.count('C')) / len(DNA) 

def calc_median(lst: list) -> float:
    '''Given a sorted list, returns the median value of the list.'''
    lst_length = len(lst) 
    if lst_length == 0:
        raise ValueError("Cannot pass empty list")
    elif lst_length % 2 == 1:
        return lst[lst_length//2]
    else:
        return (lst[lst_length//2] + lst[lst_length//2-1]) / 2

def oneline_fasta(old_filepath):
    '''Reads a given fasta file and returns a new file called 'single.fa' with every line of a sequence on the same line.'''
    with open("single.fa","w") as newfile:
        header_tracker=0
        with open(old_filepath,"r") as oldfile:
            for line in oldfile:
                if line[0] == ">" and header_tracker == 0:
                    header_tracker+=1
                    newfile.write(f"{line.strip()}\n")
                elif line[0] == ">":
                    newfile.write(f"\n{line.strip()}\n")
                else:
                    newfile.write(line.strip())
        newfile.write("\n")

def convert_fasta_to_phylip(input_fasta_path, output_phylip_path):
    """
    Converts an aligned FASTA file (like the output from MUSCLE) into a sequential PHYLIP format file.
    """
    sequences = []
    current_sequence_lines = []
    current_id = None

    print(f"Reading FASTA file: {input_fasta_path}...")

    # Step 1: Read and parse the aligned FASTA file ---
    with open(input_fasta_path, 'r') as f_in:
        for line in f_in:
            line = line.strip()
            if line.startswith('>'):
                # If we have a sequence stored, save it before starting a new one
                if current_id is not None:
                    sequences.append((current_id, "".join(current_sequence_lines)))
                
                # Start a new sequence entry
                current_id = line[1:].split()[0]  # Get ID from header, e.g., ">Seq1" -> "Seq1"
                current_sequence_lines = []
            else:
                current_sequence_lines.append(line.replace(" ", ""))
        # Append the very last sequence in the file
        sequences.append((current_id, "".join(current_sequence_lines)))

    #Step 2: Get alignment dimensions 
    num_sequences = len(sequences)
    # All sequences in an aligned FASTA have the same length
    seq_length = len(sequences[0][1])

    #Step 3: Write the output in PHYLIP format ---
    with open(output_phylip_path, 'w') as f_out:
        # Write the PHYLIP header
        f_out.write(f" {num_sequences} {seq_length}\n")

        # Write each sequence with a formatted 10-character ID
        for seq_id, sequence in sequences:
            formatted_id = f"{seq_id[:10]:<10}"
            f_out.write(f"{formatted_id} {sequence}\n")


if __name__ == "__main__":
    convert_fasta_to_phylip("/projects/bgmp/ewi/bi623/ICA3/align.afa", "align.phy")
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    # These tests are run when you execute this file directly (instead of importing it)
    
    #tests for reverse complement
    reverse_complement("ATGCCGTA")
    assert reverse_complement("ATGCCGTA") == "TACGGCAT", "wrong reverse complement"
    assert reverse_complement("ATCATGCG") == "CGCATGAT", "wrong reverse complement"
    assert reverse_complement("CTCTGGAT") == "ATCCAGAG", "wrong reverse complement"


    #tests for convert_phred
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

    #tests for qual_score
    assert qual_score("!") == 0, "wrong qual score for '!'"
    assert qual_score('"') == 1, """wrong qual score for '"'"""
    assert qual_score("#$") == 2.5, "wrong qual score for '#$'"
    assert qual_score("!I!I") == 20, "wrong qual score for '!I!I'"
    assert qual_score("IIII") == 40, "wrong qual score for 'IIII'"
    print("Your qual_score function is working! Nice job")

    #tests for validate_base_seq
    assert validate_base_seq("") == True, "wrong output for ''"
    assert validate_base_seq("8") == False, "wrong output for '8'"
    assert validate_base_seq("agTCaT") == True, "wrong output for 'agTCaT'"
    assert validate_base_seq("agUCau",True) == True, "wrong output for 'agUCau'"
    print("Your validate_base_seq function is working! Nice job")

    #tests for gc_contents
    assert gc_content("") == 0, "wrong gc content for ''"
    assert gc_content("GCGCGCGCCCCC") == 1, "wrong gc content for 'GCGCGCGCCCCC'"
    assert gc_content("GA") == 0.5, "wrong gc content for 'GA'"
    assert gc_content("GCACACTCG") == 0.6666666666666666, "wrong gc content for 'GA'"
    print("Your gc_content function is working! Nice job")

    #tests for calc_median
    try:
        calc_median([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        pass
    assert calc_median([10]) == 10, "wrong median for [10]"
    assert calc_median([10,20]) == 15, "wrong median for [10,20]"
    assert calc_median([10,20,100]) == 20, "wrong median for [10,20,100]"
    assert calc_median([-5, -3, -1]) == -3, "wrong median for [-5,-3,-1]"
    assert calc_median([-10, -4, -3, -1]) == -3.5, "wrong median for [-10,-4,-3,-1]"
    print("Your calc_median function is working! Nice job")

    #tests for oneline_fasta
    input_file = "input_content.fasta"
    expected_output = "expected_output.fasta"
    oneline_fasta(input_file)
    with open("single.fa",'r') as output, open(expected_output,'r') as expected:
        output_content = output.read()
        expected_output = expected.read()
    assert output_content == expected_output, f"Expected:\n{expected_output}\nGot:\n{output_content}"
    os.remove("single.fa")
    print("Your oneline_fasta function is working! Nice job")