import sys
def addition(a,b):
    return a+b

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print("Addition is: ", addition(a,b))