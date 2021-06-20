#sale menu


memberinput = True
while True:
    print('============================')
    print('1> SALE PRODUCT\n2> CUSTOMER SALE REPORT\n3> SALE REPORT\n4> TOTAL SALE AMOUNT')
    print('============================')


    req = int(input('Enter your menu ID :'))
    if req == 1:
        import sale_product
    elif req == 2:
        import sale_prodct_customerwise
    elif req == 3:
        import sale_report
    elif req == 4:
        import sale_amt_rept
    else :
        print('Please Enter the value in menu ID : ')
        print('*******************************')

    memberinput = input('Enter y To Continue the menu q to stop :')
    if memberinput == 'q':
        break
    else:
        print('Please Enter the value in menu ID : ')

print('Close all')





