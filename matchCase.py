a = int(input("Enter a number : "));

match a:
    case 0:
        print('0 is not a valid input.');
    case _ if(a%2 == 0):
        print(a , " is a even number.");
    case _ if(a%2!= 0 ):
        print(a," is an odd number.");
    case _:
        print("Entered value is : ",a)