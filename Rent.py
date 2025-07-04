# what we need to create this project 
# we need input such as = Total_rent and Total_foods and Electricity units spend and charge per unit 
# How many persons in living in one room 

#output - Total_amount 
####################################################################################################################

# Create inputs 
Room_rent = int(input("Enter Your Total Room Rent: "));
Food = int(input("Enter Your Amount of food ordered: "));
Electricity_spend  = int(input("Enter the Total of electricity spend: "));
Electricity_charge = int(input("Enter the charge per unit of electricity: "));
persons = int(input("Enter the number of persons living in one room: "));


#create a input for total bill price 
total_bill = Electricity_spend*Electricity_charge;
#here we total all the amount  
total = (Food + Room_rent + total_bill); 

Dividation = total / persons; 
#here we calculate the total amount per person
print("Total amount to be paid by each person is: ", Dividation);

