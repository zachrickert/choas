# A simple program to show chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = input("Enter a number between 0 and 1: ")
    number_of_iterations = input("How many numbers shoud I print? ")

    for i in range(number_of_iterations):
        x = 3.9 * x * (1-x)
        print (x)

main()
