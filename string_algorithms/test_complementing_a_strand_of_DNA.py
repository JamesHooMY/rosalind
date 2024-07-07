import pytest
from pytest_benchmark.fixture import BenchmarkFixture

# method 1
# use a hash table to store the complement of each nucleotide
# reverse the DNA sequence
# iterate through the DNA sequence and replace each nucleotide with its complement
# return the complemented DNA sequence
# TC: O(N), SC: O(N) since we are storing the complemented DNA sequence
# * This is the best solution for me currently
def complementing_a_strand_of_DNA_1(dna: str) -> str:
    """
    Complement a DNA sequence by replacing each nucleotide with its complement.

    Parameters:
    dna (str): DNA sequence.

    Returns:
    str: Complemented DNA sequence.
    """
    dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

    return ''.join(dict[base] for base in reversed(dna))

# method 2
# use a hash table to store the complement of each nucleotide
# iterate through the DNA sequence in reverse order
# replace each nucleotide with its complement
# return the complemented DNA sequence
# TC: O(N), SC: O(N) since we are storing the complemented DNA sequence
def complementing_a_strand_of_DNA_2(dna: str) -> str:
    """
    Complement a DNA sequence by replacing each nucleotide with its complement.

    Parameters:
    dna (str): DNA sequence.

    Returns:
    str: Complemented DNA sequence.
    """
    dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

    complement_dna = ''
    for i in range(len(dna) - 1, -1, -1): # start, stop, step
        complement_dna += dict[dna[i]]
    return complement_dna


dna_input: str = "CAACTAAGGGCATTATCTCCCAGCTGATGCCTGTCCCGGCCGCGTGTAGGGTTCTCTGGGTGTACAACCTCTCGAGAACACTTATAAGTGTCCCCAACCAGCGGGCTGCGCTTCGGATCTCAGTGCACGAAAAACAGATAAGGTGGTCGATATAAGCACCGAGTCTTAGGTCTAGCGGCGACTTGACACTGTATGATGTACATAGCGCGATATGTCACCGATGCGTGATTCCTGTACAATGATCCGTCTTAGCCTAACAAAAGACCCGACCGGGGATCCAGATTTGGTAAGGCAGCGGACTTGGGTGCTTAGCAGGTGAAGCTACGTCTGCGCTCAAGCCCTAGTTCCTTTTGCATAGTGCCCTGAGTATATGCGAGGCAGACATTTTCTGTCACTTATCCTACACGTCGCAGGAGCTGCCGTTGTTGCACTCTATGTGCGCCTAGGAACAAGTAACGTTGCGTAGGCCACATGGGCATAATACTAGTTCTCAACGTGGACGGTTCGACAAGCATACGGGAGCTAGTTAAGCCCGAAACGCCGATTCCCCAATTGACCACGGCGAATGGTGGTAAGCTATAGTAGTGTCGTGGCGTGGGACTCTGGCAGCGATGAGAAAGCATAACTGCCGTTCAGACTTTCTATACAAGTTCTCAGTATGGACCTATACGTGGCTCACCTTCGTTTCGAAGTCTGAGATTTCCGTACGGTCCGTTCACGGTCGCTTGATTAAGTAGTTTTCCGCTTCTCGAAGACTTCCGGGGTACTACGTAATTCATGGTCGTAGATATGACGAGCTTCCGCGCTACGTGGATTACATGATCGGGAAGTCTTAG"

expected_output: str =  "CTAAGACTTCCCGATCATGTAATCCACGTAGCGCGGAAGCTCGTCATATCTACGACCATGAATTACGTAGTACCCCGGAAGTCTTCGAGAAGCGGAAAACTACTTAATCAAGCGACCGTGAACGGACCGTACGGAAATCTCAGACTTCGAAACGAAGGTGAGCCACGTATAGGTCCATACTGAGAACTTGTATAGAAAGTCTGAACGGCAGTTATGCTTTCTCATCGCTGCCAGAGTCCCACGCCACGACACTACTATAGCTTACCACCATTCGCCGTGGTCAATTGGGGAATCGGCGTTTCGGGCTTAACTAGCTCCCGTATGCTTGTCGAACCGTCCACGTTGAGAACTAGTATTATGCCCATGTGGCCTACGCAACGTTACTTGTTCCTAGGCGCACATAGAGTGCAACAACGGCAGCTCCTGCGACGTGTAGGATAAGTGACAGAAAATGTCTGCCTCGCATATACTCAGGGCACTATGCAAAAGGAACTAGGGCTTGAGCGCAGACGTAGCTTCACCTGCTAAGCACCCAAGTCCGCTGCCTTACCAAATCTGGATCCCCGGTCGGGTCTTTTGTTAGGCTAAGACGGATCATTGTACAGGAATCACGCATCGGTGACATATCGCGCTATGTACATCATACAGTGTCAAGTCGCCGCTAGACCTAAGACTCGGTGCTTATATCGACCACCTTATCTGTTTTTCGTGCACTGAGATCCGAAGCGCAGCCCGCTGGTTGGGGACACTTATAAGTGTTCTCGAGAGGTTGTACACCCAGAGAACCCTACACGCGGCCGGGACAGGCATCAGCTGGGAGATAATGCCCTTAGTTG"

def test_complementing_a_strand_of_DNA_1():
    assert complementing_a_strand_of_DNA_1(dna_input) == expected_output
def test_complementing_a_strand_of_DNA_2():
    assert complementing_a_strand_of_DNA_2(dna_input) == expected_output

@pytest.mark.benchmark(group='complementing_a_strand_of_DNA')
def test_benchmark_complementing_a_strand_of_DNA_1(benchmark: BenchmarkFixture):
    benchmark(complementing_a_strand_of_DNA_1, dna_input)

@pytest.mark.benchmark(group='complementing_a_strand_of_DNA')
def test_benchmark_complementing_a_strand_of_DNA_2(benchmark: BenchmarkFixture):
    benchmark(complementing_a_strand_of_DNA_2, dna_input)

if __name__ == '__main__':
    pytest.main()