# def add(n1,n2):
#     print(n1+n2)
# add(10,20)
#
# number1 = 10
# #number2 = input("Please input a number: ")
# #add(number1,number2)



# try:
#     # WANT TO TRY THIS CODE
#     result = 10 + "10"
# except:
#     print("Not adding correctly")
# else:
#     print("Add went well")
#     print(result)



# try:
#     f = open("testfile","w")
#     f.write("Write a test file line")
# except TypeError:
#     print("There was a type error")
# except OSError:
#     print("Hey you have an OS Error")
# except:
#     print("All other errors")
# finally:
#     print("I always run")

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Woops thats is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
ask_for_int()