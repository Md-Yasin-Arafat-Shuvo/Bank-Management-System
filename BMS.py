NamesOFClients = ['Yasin Shuvo ', 'Badrul Akib', 'Fayjul Bappi', 'Saidul Abir', 'Mustafijur', 'johan ',
                  'karim']

ClientPins = ['0001', '0002', '0003', '0004', '0005', '0006', '0007']
ClientBalances = [100000, 200000, 300000, 400000, 500000, 600000, 700000]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
disk1 = 1
disk2 = 7
u = 0

while True:
    # os.system("cls")

    print("\t\t\t\t|       -------------------------------------       |")
    print("\t\t\t\t|       -------------------------------------       |")
    print("\t\t\t\t|       -------------------------------------       |")
    print("\t\t\t\t|      |         BANK MANAGEMENT SYSTEM  |          |")
    print("\t\t\t\t|      |              www.bb.org.bd      |          |")
    print("\t\t\t\t|       -------------------------------------       |")
    print("\t\t\t\t|      |         WELCOME TO MY BANK      |          |")
    print("\t\t\t\t|       -------------------------------------       |")
    print("\t\t\t\t|       -------------------------------------       |")

    print("(1). Open New Client Account ")
    print("(2). The Client Withdraw a Money")
    print("(3). The Client Deposit a Money")
    print("(4). Check Clients & Balance")
    print("(5). Quit ")

    EnterLetter = input("Select a Letter from the Above Box menu : ")
    if EnterLetter == "1":
        print(" Letter a is Selected by the Client")
        NumberOfClient = eval(input("Number of Clients : "))
        u = u + NumberOfClient

        if u > 7:
            print("\n")
            print("Client registration exceed reached or Client registration too low")
            u = u - NumberOfClient

        else:
            while disk1 <= u:
                name = input("Write Your Fullname : ")
                NamesOFClients.append(name)
                pin = str(input("Please Write a Pin to Secure your Account : "))
                ClientPins.append(pin)
                ClientBalance = 0
                ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
                ClientBalance = ClientBalance + ClientDeposition
                ClientBalances.append(ClientBalance)
                print("\nName=", end=" ")
                print(NamesOFClients[disk2])
                print("Pin=", end=" ")
                print(ClientPins[disk2])
                print("Balance=", "TK", end=" ")
                print(ClientBalances[disk2], end=" ")
                disk1 = disk1 + 1
                disk2 = disk2 + 1
                print("\nYour name is added to Client Table")
                print("Your pin is added to Client Table")
                print("Your balance is added to Client Table")
                print("----New Client account created successfully !----")
                print("\n")
                print("Your Name is Available on the Client list now : ")
                print(NamesOFClients)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")

        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "2":
        v = 0
        print(" letter b is Selected by the Client")
        while v < 1:

            w = -1
            name = input("Please Insert a name : ")
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:

                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        v = v + 1
                        print("Your Current Balance:", "TK", end=" ")
                        print(ClientBalances[w], end=" ")
                        print("\n")
                        ClientBalance = (ClientBalances[w])
                        ClientWithdrawal = eval(input("Insert value to Withdraw : "))
                        if ClientWithdrawal > ClientBalance:

                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))

                            ClientBalance = ClientBalance + deposition
                            print("Your Current Balance:", "TK", end=" ")
                            print(ClientBalance, end=" ")
                            ClientBalance = ClientBalance - ClientWithdrawal
                            print("-\n")
                            print("----Withdraw Successfully!----")
                            ClientBalances[w] = ClientBalance
                            print("Your New Balance: ", "TK", ClientBalance, end=" ")
                            print("\n\n")

                        else:

                            ClientBalance = ClientBalance - ClientWithdrawal
                            print("\n")
                            print("----Withdraw Successfully!----")
                            ClientBalances[w] = ClientBalance
                            print("Your New Balance: ", "TK", ClientBalance, end=" ")
                            print("\n")

            if v < 1:
                print("Your name and pin does not match!\n")
                break

        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "3":
        print("Letter c is selected by the Client")
        x = 0
        while x < 1:
            w = -1
            name = input("Please Insert a name : ")
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:

                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        x = x + 1
                        print("Your Current Balance: ", "TK", end=" ")
                        print(ClientBalances[w], end=" ")
                        ClientBalance = (ClientBalances[w])
                        print("\n")
                        ClientDeposition = eval(input("Enter the value you want to deposit : "))
                        ClientBalance = ClientBalance + ClientDeposition
                        ClientBalances[w] = ClientBalance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", "TK", ClientBalance, end=" ")
                        print("\n")

            if x < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "4":

        print("Letter d is selected by the Client")
        w = 0
        print("Client name list and balances mentioned below : ")
        print("\n")
        while w <= len(NamesOFClients) - 1:
            print("-> Customer =", NamesOFClients[w])
            print("-> Balance =", "TK", ClientBalances[w], end=" ")
            print("\n")
            w = w + 1

        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
    elif EnterLetter == "5":

        print("letter e is selected by the client")
        print("Thank you for using our banking system!")
        print("\n")
        print("Thank You and Come again")
        print("God Bless")
        break

    else:
        print("Invalid option selected by the Client")
        print("Please Try again!")

        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")