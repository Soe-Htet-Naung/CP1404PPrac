def main():

    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    for i in range(20, 0, -1):
        print(i, end=' ')
    print()
    outputStars()

def outputStars():
    n = int(input("Input any number you like : "))

    """Just to make it a bit clean in the output"""
    print("One line output")

    output = ""
    for i in range(n):
        output = output + '*'
    print(output)

    """Just to make it a bit clean in the output"""
    print("Multiple Lines Output")

    output = ""
    for i in range(n):
        output = output + '*'
        print(output)

if __name__ == '__main__':
    main()