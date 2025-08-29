try :
    with open('sample.txt','r') as f :
        print("Reading file content:")
        rf = f.readline()
        print("Line 1 :", rf.strip())
        rf = f.readline()
        print("Line 2 :", rf.strip())
except FileNotFoundError :
    print("ERROR :The file/'sample.txt' was not found")





