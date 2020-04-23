# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print("TypeError")
#
#
# try:
#     x = 5
#     y = 0
#     z = x / y
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# finally:
#     print("All done")


def ask():
    while True:
        try:
            result = int(input("Enter a number: "))
            # print(result)
            # print(type(result))
            result = result**2
        except:
            print("An error occurred!")
            continue
        else:
            print(f"Thank you your number squard is {result}")
            break
ask()