
def print_Grid():

    for p in range(5):

        if p%2==0:
            for x in range(5):

                if x%2 == 0:
                    print("+ ", end="")

                else:

                    print("- "*4, end="")

            print()
        
        else:
            for y in range(4):
                for x in range(5):

                    if x%2 == 0:

                        print("|", end="")

                    else:

                        print(" " * 9, end="")
                print()
            

print_Grid()

