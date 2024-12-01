
def accum(s: str):
    try:
        # Verify that s is string or not
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        
        # Verify that s is only composed of English letter(s) (a-z, A-Z)
        for ch in s:
            if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
                raise ValueError("Input must contain only English letters")
        
        # If input is correct the operation will continue
        result = [(ch * (idx + 1)) for idx, ch in enumerate(s)]  # multiply character with index + 1
        
        # Convert first character to Uppercase and other to Lowercase
        transformed = [
            elem[0].upper() + elem[1:].lower()  
            for elem in result
        ]
        
        # Join with "-"
        return "-".join(transformed)
    except (TypeError, ValueError) as e:
        return str(e)


# Run this file for test
assert accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
assert accum("NyffsGeyylB") == "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
assert accum("MjtkuBovqrU") == "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
assert accum("EvidjUnokmM") == "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
assert accum("HbideVbxncC") == "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"