def main():
    numbers_of_items = int(input("Please Enter the numbers of items : "))
    calculateTotal(numbers_of_items)
    while numbers_of_items < 0:
        print("Invalid number of items!")
        numbers_of_items = int(input("Please Enter the numbers of items : "))
        calculateTotal(numbers_of_items)


def calculateTotal(numbers_of_items):
    numbers_of_items = numbers_of_items
    totalPrice = 0
    for i in range(numbers_of_items):
        print("Item number", i + 1)
        price = float(input("Please Enter the price of item : "))
        totalPrice = totalPrice + price

    if totalPrice > 100:
        discount = (totalPrice / 100) * 10
        totalPrice = totalPrice - discount
    else:
        totalPrice = totalPrice

    print("Total Price is : {:.2f} $".format(totalPrice))


if __name__ == '__main__':
    main()
