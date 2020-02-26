""" 
Robert Walczak
This multiplies the string by n.
    :param message, a string
    :param n, an intiger
    :returns the message x n 
    """


def multiply_string(message,n):
    print(message*n)
    return(message*n)

if __name__=='__main__':
    multiply_string('Robert', 3)
