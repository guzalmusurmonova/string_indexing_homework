def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """ 
    if s[0].isdigit()==1:
        x1=1 
    else:
        x1=0 
    if s[1].isdigit()==1:
        x2=1 
    else:
        x2=0 
    if s[2].isdigit()==1:
        x3=1
    else:
        x3=0
    if s[3].isdigit()==1:
        x4=1
    else:
        x4=0
    if s[4].isdigit()==1:
        x5=1
    else:
        x5=0
    return x1+x2+x3+x4+x5
print(main('32x3z'))