def main(a):
    """
    check the following statement "The variable "a" is an odd number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b = a%2
    return b == 1

v = main(5)
print(v)