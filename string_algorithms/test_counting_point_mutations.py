# use zip to iterate through two sequences simultaneously and compare the nucleotides
# increment a counter if the nucleotides are different
# return the counter
# TC: O(N), SC: O(1) since we are only storing the count of point mutations
def count_point_mutations(s1: str, s2: str) -> int:
    """
    Count the number of point mutations (Hamming distance) between two DNA sequences.

    Parameters:
    s1 (str): First DNA sequence.
    s2 (str): Second DNA sequence.

    Returns:
    int: Number of point mutations.
    """
    if len(s1) != len(s2):
        raise ValueError("Sequences must be of equal length")

    return sum(1 for a, b in zip(s1, s2) if a != b)


def test_count_point_mutations():
    s1 = "GAGCCTACTAACGGGAT"
    s2 = "CATCGTAATGACGGCCT"

    assert count_point_mutations(s1, s2) == 7
    print("count_point_mutations PASSED")