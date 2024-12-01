
def word_mesh(words: list[str]):
    # Write your code here.
    """
    input list of string and process each pair of elements that next to each other
    """
    # Check for there are at least 2 elements is list
    if len(words) < 2:
        raise ValueError("The list must contain at least 2 elements.")
    
    # Verify that all elements is string type
    if not all(isinstance(element, str) for element in words):
        raise TypeError("All elements in the list must be strings.")
    
    def sub_string_forward(word: str):
        # Create sub-string forward
        return [word[idx:] for idx in range(len(word))]

    def sub_string_backward(word: str):
        # Create sub-string backward
        return [word[:idx] for idx in range(1, len(word) + 1)]

    def find_max_match(forward_list, backward_list):
        # Find maximum length match
        matching = set(forward_list) & set(backward_list)
        return max(matching, key=len, default="")  # return maximum string or blanl string if there is no match string

    # process pair of elements that next to each other
    result_string = ""
    for i in range(len(words) - 1):
        forward_substrings = sub_string_forward(words[i])
        backward_substrings = sub_string_backward(words[i + 1])
        match_string = find_max_match(forward_substrings, backward_substrings)

        # if there is no match
        if match_string == "":
            return "failed to mesh"

        result_string += match_string  # combine match string from each pair

    return result_string

# Run this file for test
assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
assert word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
assert word_mesh(["kingdom", "dominator", "notorious", "usual", "allegory"] ) == "failed to mesh"