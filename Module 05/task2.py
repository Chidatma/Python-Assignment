with open("output.txt",'a') as fh:
    data1 = input("Enter text to write to the file: ")
    fh.write(data1 + "\n")
    print("Data successfully written to output.txt.")
    data2 = input("\nEnter additional text to append: ")
    fh.write(data2 + "\n")
    print("Data successfully appended.")

with open("output.txt", 'r') as fh:
    print("\nFinal content of the file:")
    print(fh.read())