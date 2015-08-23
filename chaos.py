# A simple program to show chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = input("Enter a number between 0 and 1: ")
    y = input("Enter a second number between 0 and 1: ")
    number_of_iterations = input("How many numbers shoud I print? ")

    print
    print str("{:0.7f}".format(x)) + " | " + str("{:0.7f}".format(y))
    print "----------|----------"
    for i in range(number_of_iterations):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print str("{:0.7f}".format(x)) + " | " + str("{:0.7f}".format(y))

main()
