from playsound import playsound
playsound("D:\\1.mp3")
print("Welcome to State bank of India\n")
playsound("D:\\2_1.mp3")
playsound("D:\\2.mp3")
p=int(input("Enter your 4 digit pin number: "))
playsound("D:\\4.mp3")
m = 25000
if(p == 1234):

    print("1-Withdraw\n")

    print("2-Balance Enquiry\n")

    print("3-Fast Cash\n")

    print("4-Mini statement\n")

    print("5-Cash Deposit\n")
    
    playsound("D:\\3.mp3")
    c = int(input("Please choose transactions: "))
    if (c == 1):
        playsound("D:\\withdrawal.mp3")
        w=int(input("Enter withdraw amount: \n"))
        playsound("D:\\4.mp3")
        if (w < m and w%100 == 0):
            print("Please take your amount:", w)
            print("Amount available: ",(m - w))
        else:
            print("Invalid cash ")

    elif(c==2):
        playsound("D:\\balance.mp3")
        print("Your balance amount : ",m)

    elif (c == 3):
        print("1->5,000")
        print("2->10,000")
        print("3->15,000")
        print("4->20,000")
        playsound("D:\\fast cash.mp3")
        f = int(input("Enter fast cash option: "))
        playsound("D:\\4.mp3")
        if (f == 1 and 5000 < m):
            print("Please take cash 5000")
            print("Amount available: ",(m - 5000))
        elif (f == 2 and 10000 < m):
            print("Please take cash 10000")
            print("Amount available: ",(m - 10000))
        elif (f == 3 and 15000 < m):
             print("Please take cash 15000")
             print("Amout available: ",(m - 15000))
        elif (f == 4 and 20000 < m):
            print("Please take cash 20000")
            print("Amout available: ",(m - 20000))
        else:
            playsound("D:\\invalid fast cash.mp3")
            print("Invalid fast cash option")
    elif(c==4):
        playsound("D:\\statement.mp3")
        print(''' 
                 14/6/22 :5000 transfered to Mr.Nitin by Gpay
                 14/6/22 :10000 transfered to Mr.Mahajan by paytm
                 15/6/22 :500 transfered to Ms.tanjua by Debit Card
                 15/6/22 :10000 credited by Mr.Roshan by Phonepe
                 17/6/22 :5000 debited and transfered to Mr.piyush
                 19/6/22 :60000 credited by cheque transfer
                 19/6/22 :2000 transfered to Ms.Priya
                 20/6/22 :50000 withdraw at SBI ATm in Indira Nagar,Nashik''')
    elif(c==5):
        playsound("D:\\depositing.mp3")
        Deposit_Amount=int(input("\nEnter The Amount You Want To Deposit : "))
        playsound("D:\\4.mp3")
        print("Available Balance=",Deposit_Amount+m)
    else:
        print("Wrong choice")
else:
    playsound("D:\\incorrect pin.mp3")
    print("Wrong pin number")

