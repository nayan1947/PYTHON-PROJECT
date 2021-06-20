# stock menu

memberinput = True
while True:
    print('============================')
    print('1> ADD A NEW PRODUCT TO CART\n2> STOCK REPORT\n3> STOCK UPDATE')
    print('============================')


    req = int(input('Enter your menu ID :'))
    if req == 1:
        import product_master
    elif req == 2:
        import current_stock_report
    elif req == 3:
        import stock_update
    else:
        print('Please Enter the value in menu ID : ')
        print('*******************************')

    memberinput = input('Enter y To Continue the menu q to stop :')
    if memberinput == 'q':
        break
    else:
        print('Please Enter the value in menu ID : ')

print('Close all')





