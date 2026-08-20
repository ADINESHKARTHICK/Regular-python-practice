choice = int(input("Enter 1 for Even or 2 for Odd: "))

match choice:
    case 1:
        # Choice: Even numbers
        for i in range(100, 201):
            if i % 2 == 0:
                print(i * i)

    case 2:
        # Choice: Odd numbers
        for j in range(100, 201):
            if j % 2 != 0:
                print(j * j)

    case _:
        print("Invalid choice")
