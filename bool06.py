def main(a):
    """
    check the following statement "The variable "a" is an even number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b = a%2
    return b ==0

v = main(5)
print(v)