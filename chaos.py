# A simple program to show chaotic behavior

def main():
  print("This program illustrates a chaotic function")
  x = input("Enter a number between 0 and 1: ")
  for i in range(10):
    x = 2.0 * x * (1-x)
    print (x)

main()
