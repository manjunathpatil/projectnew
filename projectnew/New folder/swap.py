def sw(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

def main():
    a= int(input("enter the value"))
    b= int(input("entet the value"))
    print(sw(a,b))

main()
