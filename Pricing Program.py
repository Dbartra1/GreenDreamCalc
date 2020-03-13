#!/usr/bin/env python3
##For use by Green Dream Cannabis (Health Services LLC)
##Authored By Dillon Forrest Bartram

from decimal import Decimal
import locale as lc

def disclaimer ():
    print (("\n")+("Copyright Disclaimer: \nUnder section 107 of the Copyright Act of 1976, allowance is made for “fair use” for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research.\n")+
          ("Fair use is a use permitted by copyright statute that might otherwise be infringing.\n\n")+
          ("Fair Use Definition: \n") +
          ("Fair use is a doctrine in United States copyright law that allows limited use of copyrighted material without requiring permission from the rights holders,\n") +
          ("such as commentary, criticism, news reporting, research, teaching or scholarship. It provides for the legal, non-licensed citation or incorporation of copyrighted material in another author’s work under a four-factor balancing test.\n"))

def options():
    selection = ["1. Employee Pricing","2. Customer Post-Tax Pricing","3. Product Cost & Margin","4. Exit"]
    print(*selection, sep = "\n")

def get_emp_pricing(item_price, qty, tax_rate, emp_rate):
    emp_rate = float(1.25)
    tax_rate = float(1.20587)
    rate_total = item_price * emp_rate
    print ("\nRate total", round(rate_total,2))
    tax_total = item_price * tax_rate
    print ("Tax total", round(tax_total,2))
    emp_price = ((rate_total + tax_total) - (item_price)) * qty
    print ("Emp price", round(emp_price,2))
    return round(emp_price, 2)

def get_cust_price(tax_rate, item_price, qty_cust):
    tax_rate = float(1.20587)
    cust_price = (tax_rate * item_price) * qty_cust
    return round(cust_price, 2)

def get_case_margin(wholesale_price, case_qty, qty_wholesale, otd_price):
    case_price = wholesale_price * case_qty
    print ("\ncase price: ", round(case_price,2))
    case_price_retail = case_qty * otd_price
    print ("case price retail: ", round(case_price_retail,2))
    profit = case_price_retail - case_price
    print ("profit per case: ", round(profit,2))
    margin_per = profit / case_price_retail
    return round(margin_per, 2)

def main():
    disclaimer()
    print ()
    print("----------Green Dream Guided Calculator----------", "\n")
    options()
    while True:
        res = input("\nWhat Would You Like To Calculate?: ").strip().lower()
        if res == '1':
            choice = "y"
            while choice.lower() == "y":
                print()
                tax_rate = float(1.20587)
                emp_rate = float(1.25)
                item_price = float(input("What Is Our Price On Flowhub? (Found In Flowhub Under Activity): "))
                qty = int(input("\nHow Many of This Item Are You Buying?: "))
                emp_price = get_emp_pricing (item_price, qty, tax_rate, emp_rate)
                print ("Item Price:\t\t" + str(item_price))
                print ("QTY:\t\t\t" + str(qty))
                print ("Employee Price:\t\t" + str(emp_price))
                print ()
                choice = input("Continue? (y/n): ").strip().lower()
                print()
                if choice == "n":
                    main()
        if res == '2':
            choice = "y"
            while choice.lower() == "y":
                tax_rate = float(1.20587)
                item_price = float(input("\nWhat Is The Price On Cashier?: "))
                qty_cust = float(input("\nHow Many Are They Buying?: "))
                cust_price = get_cust_price(tax_rate, item_price, qty_cust)
                print ("\nOut The Door Customer Price: ", round(cust_price,2))
                print ('\n')
                choice = input("Continue? (y/n): ").strip().lower()
                print()
                if choice == "n":
                    main()   
        if res == '3':
            while True:
                res2 = input("\nBy The Case Or By Individual Unit? [C/U]: ")
                if res2 == "C":
                    wholesale_price = (float(input("What Did We Pay Wholesale Per Item?: ")))
                    case_qty = (float(input("How Many Per Case?: ")))
                    qty_wholesale = (float(input("How Many Cases Did We Buy?: ")))
                    otd_price = (float(input("What Do We Want To Charge Per Item?: ")))
                    margin_per = get_case_margin(wholesale_price, case_qty, qty_wholesale, otd_price) *100
                    print ("Profit Margin", round(margin_per,2), chr(37))
                if res2 == "U":
                    wholesale_price = (float(input("What Did We Pay Wholesale Per Item?: ")))
                    otd_price = (float(input("What Do We Want To Charge Per Item?: ")))
    
        if res == '4':
            print ('Peace OOOOUT!')
        else:
            print ("\nSorry Foo Thats Not A Valid Input, Try Again!!")
        
main()

            
