from deffunc import *



df = pd.read_csv("priyansh.csv")



cn = sqlconn.connect(database='mysql', host='localhost', user='root', password='1234')
cursor = cn.cursor()
whyus = ('\n\n1)IAU offers tremendous growth opportunities.'
         '\n\n2)IAU have respect in society, since there is'
         ' direct interaction with the customers.'
         '\n\n3) One of the major reason is challenging working environment, better understanding, we treat customers like our family etc.'
         '\n\n5)IAU are now using the best available technology for'
         'their work, employees get the work on the latest banking'
         'software which adds good weight age to their profile.'
         '\n\n6)Overall banks provide opportunities for higher learning'
         '\n\n7) IAU provides all banking products and also the many advantages. IAU strongly believes it is the bank for people.'
         '\n\n8)IAU fulfill the requirements and believe that It fits the customers culture well.')




e4=0
e5=0

if cn.is_connected() == False:
    print('connection failed')
else:
    while True:
        print('\t\t\t-----------------------')
        print('\t\t\t| Welcome To IAU Bank  |')
        print('\t\t\t-----------------------')
        print("\n\n---------------")
        print('|(1) Old User |')
        print('---------------')
        print('|(2) New User |')
        print('---------------')
        print('|(3) Exit     |')
        print('---------------')
        a = int(input('=>'))

        if a == 1:
            b = input("\n\nEnter Your account number:")
            print("___________________________________")
            beep()
            e2=b
            m1 = "select Account_Number from account_info where Account_Number = " + b
            cursor = cn.cursor()
            cursor.execute(m1)
            rows = cursor.fetchone()
            d = rows
            q = "select Cust_ID from account_info where Account_Number = " + b
            cursor = cn.cursor()
            cursor.execute(q)
            rows = cursor.fetchone()
            custids = rows
            for a in custids:
                custid = str(a)
            e1=custid
            if d == None:
                print('\n\nWrong Account Number')
                print("____________________")
                beep1()
            else:
                for row in d or []:
                    ac = row
                acno = int(ac)

                if int(b) == acno:

                    c = input("\nEnter Your Pin : ")
                    print('___________________________')
                    beep()
                    p1 = "select Pin from account_info where Account_Number = " + b
                    cursor = cn.cursor()
                    cursor.execute(p1)
                    rows = cursor.fetchone()
                    d = rows
                    c1 = int(c)
                    if c1 not in d:
                        print('\n\nWrong Pin')
                        print("_________")
                        beep1()

                    else:
                        z = "select Name from accounts_info where Cust_ID = " + custid
                        cursor = cn.cursor()
                        cursor.execute(z)
                        rows = cursor.fetchone()
                        d = rows
                        for row in d:
                            name = row
                        e3=name
                        print('\n\n\n\n--------------------------------------------------------')
                        print("\t\t\t   Welcome ", name ,sep='')
                        print('--------------------------------------------------------')
                        ch = 0
                        while ch != 5:
                            menu()
                            ch = int(input("Enter Your choice: "))
                            if ch == 1:
                                print('\n\n\t\t\t_________')
                                print('\n\t\t\t DEPOSIT')
                                print('\t\t\t_________')
                                print('\n\nHow Much Amount Would you Like To Deposit ?')
                                q = input('=> ₹')
                                z = "select Balance from account_info where Account_Number = " + b
                                e4=int(q)+e4
                                cursor = cn.cursor()
                                cursor.execute(z)
                                rows = cursor.fetchone()
                                d = rows
                                s = "update account_info set Balance = Balance + " + q + " Where Account_number = " + b;
                                cursor = cn.cursor()
                                cursor.execute(s)
                                cn.commit()
                                print('\n\n-------------------------------')
                                print('|Amount Deposited successfully|')
                                print('-------------------------------')
                                beep()
                            elif ch == 2:
                                print('\n\n\t\t\t__________')
                                print('\n\t\t\tWITHDRAWAL')
                                print('\t\t\t__________')
                                print('\n\nHow Much Amount Would you Like To Withdraw ?')
                                e = input('=> ₹')
                                z = "select Account_Type from account_info where Account_Number = " + b
                                cursor = cn.cursor()
                                cursor.execute(z)
                                rows = cursor.fetchone()
                                d = rows
                                for row in d:
                                    acctype = row
                                    acct = str(acctype)
                                z = "select Balance from account_info where Account_Number = " + b
                                cursor = cn.cursor()
                                cursor.execute(z)
                                rows = cursor.fetchone()
                                d = rows
                                for row in d:
                                    balance = row
                                bal1 = int(balance)
                                if 'C' == acct or 'c' == acct :
                                        pp = "update account_info set Balance = Balance - " + e + " Where Account_Number = " + b;
                                        cursor = cn.cursor()
                                        cursor.execute(pp)
                                        cn.commit()
                                        print('\n\n---------------------------------')
                                        print('| Amount Withdrawn successfully |')
                                        print('---------------------------------')
                                        beep()
                                else:
                                    if int(e) > bal1:
                                        print('\n\n----------------------------------')
                                        print('| You Can\'t Withdraw High Amount |')
                                        print('----------------------------------')
                                        beep1()
                                e5=int(e)+e5
                            elif ch == 3:
                                print('\n\n\t\t\t_______')
                                print('\n\t\t\tBALANCE')
                                print('\t\t\t_______')
                                z = "select Balance from account_info where Account_Number = " + b
                                cursor = cn.cursor()
                                cursor.execute(z)
                                rows = cursor.fetchone()
                                d = rows
                                for row in d:
                                    balance = row
                                bal1 = int(balance)
                                bbo=str(bal1)
                                fs=1
                                ss=1
                                ts=4    
                                if len(bbo) == 4:
                                    print('\n\n---------------------------------------------')
                                    print('\t   Your Balance Is : ₹',bbo[0:fs],',',bbo[ss:ts],sep='')
                                
                                    print('---------------------------------------------') 
                                    beep()
                                elif len(bbo) == 5:
                                    print('\n\n---------------------------------------------')
                                    print('\t   Your Balance Is : ₹',bbo[0:fs+1],',',bbo[ss+1:ts+2],sep='')
                                    print('---------------------------------------------')     
                                    beep()
                                elif len(bbo) == 6:
                                    print('\n\n---------------------------------------------')
                                    print('\t   Your Balance Is : ₹',bbo[0:1],',',bbo[1:fs+2],',',bbo[ss+2:ts+4],sep='')
                                    print('---------------------------------------------')
                                    beep()
                                elif len(bbo) == 7:
                                    print('\n\n---------------------------------------------')
                                    print('\t   Your Balance Is : ₹',bbo[0:2],',',bbo[2:fs+3],',',bbo[ss+3:ts+6],sep='')
                                    print('---------------------------------------------')
                                    beep()
                            elif ch == 4:
                                print('\n\n--------------------------------')
                                print('|\t\t\t   MAD                       |')
                                print('------------------------------------')
                                ch_update = 0

                                while ch_update != 6:
                                    beep()
                                    menu1()
                                    ch_update = int(input("Enter your choice: "))

                                    if ch_update == 1:
                                        Nam = input("=>")
                                        sql = "Update account_info set Name = '" + Nam + "'Where Cust_Id = " + custid;
                                        sql1 = "Update accounts_info set Name = '" + Nam + "' Where Cust_Id = " + custid;
                                        sql2 = "Update customer_info set Name = '" + Nam + "'Where Cust_Id = " + custid;
                                        cursor.execute(sql)
                                        cursor.execute(sql1)
                                        cursor.execute(sql2)
                                        cn.commit()
                                        cn.commit()
                                        cn.commit()
                                    elif ch_update == 2:
                                        regno = input("=>")
                                        while len(regno)>10 or len(regno)<10:
                                            print('\nInvaild Number')
                                            beep1()
                                            regno=input('Enter Your Registered Number Again => ')
                                        sql = "Update accounts_info set Reg_Number = '" + regno + "' Where Cust_ID = " + custid;  
                                        cursor.execute(sql)
                                        cn.commit()
                                        while len(regno)>10 or len(regno)<10:
                                            print('\nInvaild Number')
                                            beep1()
                                            regno=input('Enter Your Father\'s Number Again => ')    
                                            sql = "Update accounts_info set Reg_Number = '" + regno + "' Where Cust_ID = " + custid;  
                                            cursor.execute(sql)
                                            cn.commit()

                                    elif ch_update == 3:
                                         pin = input("=>")
                                         while len(pin) !=6:
                                             print("\nInvaild Pin")
                                             beep1()
                                             pin = input("Enter Your New Pin Again => ")
                                         sql = "Update account_info set Pin = " + pin + " Where Cust_ID = " + custid;
                                         cursor.execute(sql)
                                         cn.commit()

                                    elif ch_update == 4:
                                        acct = input("=>")
                                        while acct not in "CcSs":
                                            print('\nInvalid Input')
                                            beep1()
                                            acct = input('Enter Your Account Type (C/S) Again => ')   
                                        sql = "Update account_info set Account_Type = '" + acct + "' Where Cust_ID = " + custid;
                                        cursor.execute(sql)
                                        cn.commit()

                                    elif ch_update == 5:
                                        add = input("=>")
                                        sql = "Update accounts_info set Address = '" + add + "' Where Cust_ID = " + custid;
                                        cursor.execute(sql)
                                        cn.commit()
                                    elif ch_update>5: 
                                        print()
                                        print("Updation Completed")   
                                        beep()
                                    else:
                                        print('')
                                        print('\n\n----------------')
                                        print('|Record Updated|')
                                        print('----------------')
                                        beep()
                        beep()
                        e6=times()
                        row_contents = [e1,e2,e3,e4,e5,e6]
                        append_list_as_row("D:\\Ritansh\\Projects\\Class XII\\Ip class 12 pro\\priyansh.csv", row_contents)
                        a=e4
                        b=e6
                        c=e5
                        d=e6
                        # pl.plot(a,b)
                        # pl.plot(c,d)
                        # pl.show()
    ######################################################################################################################################################################################################
        elif a == 2:
            print('\n\n\t\t\t-----------------------')
            print('\t\t\t| Welcome To IAU Bank |')
            print('\t\t\t-----------------------')

            print('\n\n1. Create a New Account\n2. Why Choose Us ?')
            d = int(input('=>'))
            
            if d == 1:
                # cd1=str(cd)
                a = input('Enter Your Name => ')      
                while '0' in a or '1' in a or '2' in a or '3' in a or '4' in a or '5' in a or '6' in a or '7' in a or '8' in a or '9' in a: 
                    print("\nYour User Name and Password is important. That's not the right one. Try again with the right one this time.")
                    a = input('Enter Your Name Again => ')

                b = input('Enter Your Gender(M/F) => ')
                while b not in "MmFf":#space error
                    print('\nInvalid Input')
                    b = input('Enter Your Gender(M/F) Again => ')   
                c = input('Enter Your Date Of Birth (YYYY-MM-DD) => ')
                while c[0:4]>'2002' :
                    print('\nInvaild Year You Must Be 18 And Above')
                    c = input('Enter Your Date Of Birth Again (YYYY-MM-DD) => ')  
                while c[5:7]>'12' :   
                    print('\nInvaild Month')
                    c = input('Enter Your Date Of Birth Again (YYYY-MM-DD) => ')
                m1 = "select MAX(Cust_ID) from customer_info"
                cursor = cn.cursor()
                cursor.execute(m1)
                rows = cursor.fetchone()
                q = rows
                for i in q:
                    q = int(i)
                q+=1
                q=str(q)
                h=input("Enter Your 6 digit Pin => ")
                while len(h)!=6:
                    print("Invaild Entry")
                    h=input("Enter Your 6 digit Pin Again => ")
                ############################################################
                i=input("How Much Money Would You Like To Deposit => ")
                j=input("Enter Your Account Type (C/S) => ")
                while j not in 'CS' :
                    print("Invaild Input")
                    j=input("Enter Your Account Type (C/S) Again => ")
                g = input('Enter Your Number => ')
                while len(g)>10 or len(g)<10:
                    print('\nInvaild Number')
                    g=input('Enter Your Number Again => ')  
                address=input("Enter your address under 50 characters => ")
                while len(address)>=50:
                    address=input("Enter your address under 50 characters Again => ")
                accnostr=random_with_N_digits()
                Accno="select Account_Number from account_info where Account_Number like  " + str(accnostr)
                cursor = cn.cursor()
                cursor.execute(Accno)
                rows = cursor.fetchone()
                S = rows
                for z in S or []:
                    S=str(z)
                while S==Accno:
                    Accno=random_with_N_digits()
                s = "insert into customer_info values ('" + q + "','" + a + "','" + b + "','" + c + "','"+ address +"','"+ g +"')"
                cursor.execute(s)
                cn.commit()
                s1 = "insert into accounts_info values ('" + q + "','" + a + "','" + g + "','" + address +"')"
                cursor.execute(s1)
                cn.commit()
                s2 = "insert into account_info values ('" + q + "','" + a + "','" + str(accnostr) + "','"+ h +"','"+ i +"','" + j +"')"
                cursor.execute(s2)
                cn.commit()
                print('RECORD ADDED')
                print('Account No: {}\tCustomer_ID:{}\tName:{}'.format(accnostr,q,a))
                
                
                
       
            elif d == 2:
                print(whyus)
                pl.plot([0,1,2,3,4,5,6,7],[0,1,4,9,10,8,11,13])
                pl.axis([0,10,0,20]) 
                pl.xlabel("years")
                pl.ylabel("Profit(Cr.)")
                pl.show()

            elif d == 3:
                break
