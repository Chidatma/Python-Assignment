try:
    with open("sample.txt",'r') as fh:
        content = fh.read()
        print(content)
except:
    print("Error: The file 'sample.txt' was not found.")