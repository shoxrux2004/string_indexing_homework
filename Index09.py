def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0]=="0":
        return 0
    if s[0]=="1":
        return 1
    if s[0]=="2":
        return 2
    if s[0]=="3":
        return 3
    if s[0]=="4":
        return 4
    if s[0]=="5":
        return 5
    if s[0]=="6":
        return 6
    if s[0]=="7":
        return 7
    if s[0]=="8":
        return 8
    if s[0]=="9":
        return 9
    return False
print(main("7"))
print(main("k"))