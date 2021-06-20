#dealer menu

#customer menu

memberinput = True
while True:
    print('============================')
    print('1> CREATE A NEW CUSTOMER\n2> CUSTOMER REPORT\n3> CUSTOMER INFORMATION UPDATE\n4> DELETE CUSTOMER')

    print('============================')


    req = int(input('Enter your menu ID :'))
    if req == 1:
        import create_customer
    elif req == 2:
        import customer_report
    elif req == 3:
        import cust_info_update
    elif req == 4:
        import delete_customer
    else:
        print('Please Enter the value in menu ID : ')
        print('*******************************')

    memberinput = input('Enter y To Continue the menu q to stop :')
    if memberinput == 'q':
        break
    else:
        print('Please Enter the value in menu ID : ')

print('Close all')





