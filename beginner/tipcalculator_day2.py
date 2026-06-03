print("welcome to the tip calculator!!!")
total_bill=int(input("what was the total bill?:"))
tip=int(input("how much tip would you like to give 10 , 12 or 15 percent?"))
num=int(input("how many people are there to split?:"))
x=((total_bill*tip)/100)+total_bill
final_bill=x/num
print("The final amount each person should pay is:",final_bill)