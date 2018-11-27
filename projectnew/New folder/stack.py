def push(my_list):
    ele=eval(input("enter the element : "))
    my_list.append(ele)
    return my_list

def fun(l):
     if(l== []):
          print("there is no element in stack")
     else:
        l.pop()
        return l

def fun1(a,ele):
    return l

def display(mylist):
    print(mylist)

def main():
    my_list=[]
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.exit")
    a= eval(input("enter the  your choice"))
    l=[]
    while(a<4):
        if (a==1):
            l =push(my_list)
            print(l)
        elif(a==2):
            l = fun(l)
            print(l)
        elif(a==3):
            display(l)
            break
            # ele = eval(input[1, 2, 3])
            # my_list.append(ele)
        elif(a==4):
            exit(1)
        a = eval(input("enter the  your choice"))

# break


main()
