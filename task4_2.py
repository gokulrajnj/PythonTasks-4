a=input("ENTER INPUT TO WRITE ON FILE : ")
with open("output.txt","w") as f:
    f.write(a)
    print("Data succesfully written to output.txt.")
f.close()
a=input("ENTER ADDITIONAL TEXT  TO APPEND : ")
with open("output.txt","a") as f:
    f.write("\n"+a)
    print("Data appended successfully")
f.close()
with open("output.txt","r") as f:
    print(f.read())

