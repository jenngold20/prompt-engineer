#using this list [100, 200, 300] i want to obtain all the posibles permutations of this numbers

def get_permutations(list_numbers):
    permutations = []
    _get_permutations(list_numbers, [], permutations)
    return permutations
    def _get_permutations(list_numbers, current_perm, permutations):
        if not list_numbers:
            permutations.append(current_perm.copy())
            return
        
        for i, num in enumerate(list_numbers):
            current_perm.append(num)
            _get_permutations(list_numbers[:i] + list_numbers[i+1:], current_perm, permutations)
            current_perm.pop()
            return permutations
            print(get_permutations([100, 200, 300]))
            