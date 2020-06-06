# Problem Set 4A
# Name: <Ahmed Ali Mohamed>
# Collaborators: None

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # N is len(sequence)
    #the base case, no more recursion
    # return one charchter as a sinlge string element of a list
    if len(sequence) == 1:
        return [sequence]
    #get the permutations of the sequence N-1
    perms = get_permutations(sequence[1:])
    #get the first charchter to add itin every possible index of N-1 permutations to get N permutation
    first_char = sequence[0]
    #store all result of permutations to be the return value of the function
    result = [] 
    #to get the permutation of sequence N, add the first left charchter to the permutations of sequence N-1 
    for perm in perms:
        #add the first charchter to one of the sequence N-1 permutations
        #we construct the range containing len(perm)+! because
        # becaue we want to insert the first chrachter in the beginning of a permutation and at the end and each index in betwee
        for i in range(len(perm)+1):
            result.append(perm[:i]+first_char+perm[i:])
    #the return value is list of all permutatoins
    return result

if __name__ == '__main__':
    print("UNIT TESTING")
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    #example 2
    print("----------------------------------------------------------------------------------")
    input2 = "aLi"
    print("Input 2 is:", input2)
    print("expected output2 is: ['aLi', 'aiL', Lai', 'Lia', 'iaL', iLa']")
    print("Actual output2 is:", get_permutations(input2))
