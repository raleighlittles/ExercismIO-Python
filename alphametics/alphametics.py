import itertools
import re

# The technique used here is just simple brute-force, just try every permutation possible.
# There is probably a more elegant approach that uses backtracking but I couldn't figure it out.
def solve(puzzle):
    letters_to_solve_for = extract_letters(puzzle)

    # The set of available numbers to solve for. In this case there is no restriction so this set is 0123456789
    number_set: str = ''.join([str(i) for i in range(0, 10)])

    individual_letters = list(set([letter for word in letters_to_solve_for for letter in word]))

    # Only 10 numbers means that puzzles have to use 10 or less letters.
    assert (len(individual_letters) <= len(number_set))

    for permutation in itertools.permutations(number_set, len(individual_letters)):
        # Replace the letters in the puzzle string that you were given with the numbers in the permutation
        translation_object = str.maketrans(''.join(individual_letters), ''.join(permutation))

        # A representation of the puzzle equation with its letters replaced with numbers.
        translated_equation = puzzle.translate(translation_object)

        if (is_first_letter_of_word_zero(translated_equation) == False) and (eval(translated_equation)):
            return construct_answer(individual_letters, list(permutation))


"""
Extracts letters only out of the puzzle.
"""
def extract_letters(puzzle: str) -> list:
    # Python doesn't yet have an 'alphabetic-only' character class
    return re.findall(r"[a-zA-Z]+", puzzle)


"""
Constructs the dictionary representation of the form {letter : value}.
"""
def construct_answer(letters: list, numbers: list) -> dict:
    answer = dict()
    for letter_index, letter in enumerate(letters):
        answer[letter] = int(numbers[letter_index])

    return answer


"""
Due to carry rules with addition, the number value of the first letter cannot start with a 0.
Consider the addition of two 2-digit numbers, `xy` and `wz` with sum `ab`.

    xy 
  + wz
  ------
    ab 

If `a` = 0, then it must mean that `x` and `w` are 0 as well (since we're restricted to positive numbers
in this problem), in which case the addition would just simplify to `y + z = b`.    
    
"""
def is_first_letter_of_word_zero(puzzle_equation_with_numbers: str) -> bool:
    for number in puzzle_equation_with_numbers.split():
        if number[0] == str(0):
            return True

    return False
