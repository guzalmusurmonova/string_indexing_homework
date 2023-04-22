def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """ 
    if s[0]=="*": 
        x=0
    if s[1]=="*": 
        x=1
    if s[2]=="*": 
        x=2 
    if s[3]=="*": 
        x=3 
    return s[0]=="*" and x or s[1]=="*" and x or s[2]=="*" and x or s[3]=="*" and x 
print(main('good'))        