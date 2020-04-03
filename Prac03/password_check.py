def main():
    password = input("Please enter Password: ")
    get_password(password)

def get_password(password):
    output = ""
    for i in password:
        output += "*"
    print(output)

if __name__ == '__main__':
    main()