def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a > 0 and type(1)==type(a) #int ==type(a)
   
v = main(-1)
print(v)