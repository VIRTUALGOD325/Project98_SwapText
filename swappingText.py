def swap_text():
    file1 = input("Enter File1 Name: ")
    file2 = input("Enter File2 Name: ")

    with open(file1,'r') as a:
        data_a = a.read()

    with open(file2,'r') as a:
        data_b = a.read()

    with open(file1,'w') as a:
        a.write(data_b)
    
    with open(file1,'w') as a:
        a.write(data_a)
    
    print("Data Swapped Successfully")

swap_text()