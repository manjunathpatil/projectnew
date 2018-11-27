def addnumbers(add_list):
    return sum (add_list)


def main():
    add_list = []
    num = eval(input("enter the number of values to add"))
    count = num
    while(count != 0):
        ele= eval(input("enter the number"))
        add_list.append(ele)
        count = count - 1
    print(addnumbers(add_list))

main()


