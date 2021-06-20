#dealer menu


memberinput = True
while True:
    print('============================')
    print('1> Dealer Master\n 2> Dealer Payment\n 3> Dealer Report\n '
          '4> Dealer Info Update\n 5> Dealer Payment Report\n '
          '6> Delete Dealer\n 7> Delete Dealer Payment\n 8> Dealer Bill')
    print('============================')


    req = int(input('Enter your menu ID :'))
    if req == 1:
        import dealer_master
    elif req == 2:
        import dealer_payment
    elif req == 3:
        import dealer_report
    elif req == 4:
        import dealer_info_update
    elif req == 5:
        import dealer_payment_report
    elif req == 6:
        import delete_dealer
    elif req == 7:
        import delete_Dpayment
    elif req == 8:
        import bill_master
    else:
        print('Please Enter the value in menu ID : ')
        print('*******************************')

    memberinput = input('Enter y To Continue the menu q to stop :')
    if memberinput == 'q':
        break
    else:
        print('Please Enter the value in menu ID : ')

print('Close all')
print('************************')





