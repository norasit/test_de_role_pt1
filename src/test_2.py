
def reverse_string(s: str):
    # Write your code here.
    # Do not use list reverse method
    try:
        # Verify that s is string or not
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        
        # Reverse string manually
        res = ''
        for i in range(len(s)-1, -1, -1):
            res = res + s[i]
        return res
    
    except TypeError as e:
        return str(e)

assert reverse_string("abcd") == "dcba"
assert reverse_string("a3bE5dQPos") == "soPQd5Eb3a"
assert reverse_string("aka$aka") == "aka$aka"
