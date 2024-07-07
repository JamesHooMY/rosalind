import pytest
from pytest_benchmark.fixture import BenchmarkFixture

# method 1
# use zip to iterate through two sequences simultaneously and compare the nucleotides
# increment a counter if the nucleotides are different
# return the counter
# TC: O(N), SC: O(1) since we are only storing the count of point mutations
def count_point_mutations_1(s1: str, s2: str) -> int:
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

# method 2
# use a for loop to iterate through the DNA sequences
# compare the nucleotides at each index
# increment a counter if the nucleotides are different
# return the counter
# TC: O(N), SC: O(1) since we are only storing the count of point mutations
# * This is the best solution for me currently
def count_point_mutations_2(s1: str, s2: str) -> int:
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

    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

s1: str = "GAGCCTACTAACGGGAT"
s2: str = "CATCGTAATGACGGCCT"
count: int = 7

def test_count_point_mutations_1():
    assert count_point_mutations_1(s1, s2) == count

def test_count_point_mutations_2():
    assert count_point_mutations_2(s1, s2) == count


@pytest.mark.benchmark(group='count_point_mutations')
def test_benchmark_count_point_mutations_1(benchmark: BenchmarkFixture):
    benchmark(count_point_mutations_1, s1, s2)

@pytest.mark.benchmark(group='count_point_mutations')
def test_benchmark_count_point_mutations_2(benchmark: BenchmarkFixture):
    benchmark(count_point_mutations_2, s1, s2)

if __name__ == '__main__':
    pytest.main()