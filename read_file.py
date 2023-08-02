#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    list1=[]
    f=open(filename)
    a=f.read()
    b=a.split(",")
    for i in b:
        list1.append(int(i))
    return list1
#Print list from file
print(read_file("data.txt"))