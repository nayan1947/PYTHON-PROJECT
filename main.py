# main menu

print ('.....PROJECT ON STOCK AND SALES.....')
memberinput = True
while True:
    print('============================')
    print('1> DEALER MENU\n2> CUSTOMER MENU\n3> SALE MENU\n4> STOCK MENU')
    print('============================')


    req = int(input('Enter your menu ID :'))
    if req == 1:
        import dealer_menu
    elif req == 2:
        import customer_menu
    elif req == 3:
        import sale_menu
    elif req == 4:
        import stock_menu
    else :
        print('Please Enter the value in menu ID : ')
        print('*******************************')

    memberinput = input('Enter y To Continue the menu q to stop :')
    if memberinput == 'q':
        break
    else:
        print('Please Enter the value in menu ID : ')

print('Close all')





