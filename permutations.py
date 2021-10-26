#!/usr/bin/env python3

"""
    Permutations without duplicates using swap elements & recursion
"""

def generate_permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A[:])
            return

        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result

"""
    Permutations without duplicates using next_permutation() logic
"""


def next_permutation(a):
    inversion_point = len(a) - 2

    while inversion_point >= 0 and a[inversion_point] >= a[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point + 1, len(a))):
        if a[i] > a[inversion_point]:
            a[i], a[inversion_point] = a[inversion_point], a[i]
            break

    a[inversion_point + 1: ] = reversed(a[inversion_point + 1: ])
    return a


def generate_permutations_1(A):
    result = []

    while True:
        result.append(A.copy())
        A = next_permutation(A)
        if not A:
            break
    return result


"""
    Permutations when the input contains duplicates
"""

def build_char_freq_map(A):
    freq_map = {}
    for e in A:
        if e in freq_map:
            freq_map[e] += 1
        else:
            freq_map[e] = 1

    return freq_map


def duplicate_permutations(char_freq_map, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix.copy())
        return
    for e in char_freq_map:
        count = char_freq_map[e]
        if count > 0:
            char_freq_map[e] = count - 1
            duplicate_permutations(char_freq_map, prefix + [e], remaining - 1, result)
            char_freq_map[e] = count



def generate_permutations_dups(A):
    result = []
    char_freq_map = build_char_freq_map(A)
    duplicate_permutations(char_freq_map, [], len(A), result)
    return result



def main():
    # A = [1, 2, 3]
    # print(generate_permutations(A))
    # print(generate_permutations_1(A))

    A = [2, 2, 0, 3]
    print(generate_permutations_dups(A))


if __name__ == "__main__":
    main()
