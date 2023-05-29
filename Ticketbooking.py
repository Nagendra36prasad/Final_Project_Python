class movie_ticket:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.user_detials ={}
        


    def show_the_seats(self):
        
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if i == 0 and j == 0:
                    print("",end=" ")
                elif i == 0:
                    print(j,end=" ")
                elif j == 0:
                    print(i,end=" ")  
                else:
                    print("s",end=" ")
            print() 

    def Buy_a_ticket(self):
        row =int(input("enter a row number to book your seat :")) 
        column =int(input("enter a column number to book your seat :")) 
        
        total_seats = self.rows*self.columns
        if total_seats<60:
            seat_price = 10
        else:
            if row<(self.rows//2):
                seat_price = 10
            else:
                seat_price = 8        
        seat_num = str(row)+str(column)
        choise = int(input(f"welcome to book my show your opted seat number.{seat_num} and price of that seat is Rs-{seat_price}.If you still wish to book the ticket, please enter \n1.yes \n2.no : \n"))
        if choise == 1:
            name = input("Enter your name : ")
            Phone_num = int(input("Enter your phone number : "))
            gender = input("enter your gender(M/F/O): ")
            age =int(input("Enter your age : "))
            self.user_detials[seat_num] = [name,age,gender,Phone_num,seat_price]
            print(self.user_detials, "\n !! your ticket booked successfully !!")

        else:
            print("No Problem! Thank You for connecting with Book My Show!!!")    



    def statistics(self):
        seat_price = 10
        price_lst = []
        for k,v in self.user_details.items():
            price_lst.append(v[3])

        current_income = sum(price_lst)
       
        total_seats = self.rows*self.columns
        
        if total_seats <= 60:
            total_income = total_seats * 10  
        else:
            front_price = 10
            back_price = 8
            front_seats = (self.rows//2)*self.columns
            back_seats = total_seats-front_seats
            total_income = front_seats * front_price + back_seats * back_price

        num_tickets_booked = len(self.user_detials)

        percentage = (num_tickets_booked/total_seats)*100
        current_income = num_tickets_booked*seat_price
        total_income = total_seats*seat_price
        print("Number of perchased tickets : ",num_tickets_booked)
        print("Percentage of ticket booked : ",'{:.2f}%'.format(percentage))
        print("Current income : ",current_income)
        print("Total income",total_income)


    def  user_info(self):
        rows=int(input("Enter the row number of seat for which you want the info. : "))
        column=int(input("Enter the coloumn number of seat for which you want the info. : "))
        seat_num = str(rows)+str(column) 
        if seat_num in self.user_detials.keys():
            user = self.user_detials[seat_num]
            print(f"name:",user[0])
            print(f"age:",user[1])
            print(f"Gender:",user[2])
            print(f"Phone number:",user[3])
            print(f"Ticket price:",user[4])
        else:
            print(f"The seat number you were looking for has not been booked!!!")









        


           









                

