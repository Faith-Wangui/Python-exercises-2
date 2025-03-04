def calculate_electricity_bill():
    
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    units_consumed = int(input("Enter Units Consumed: "))
    
    if units_consumed <= 199:
        charge_per_unit = 1.20
    elif 200 <= units_consumed < 400:
        charge_per_unit = 1.50
    elif 400 <= units_consumed < 600: 
        charge_per_unit = 1.80
    else:
        charge_per_unit = 2.00
    
    total_bill = units_consumed * charge_per_unit
    
    if total_bill > 400:
        surcharge = total_bill * 0.15
        total_bill += surcharge
    
    if total_bill < 100:
        total_bill = 100
    
    print("\nElectricity Bill")
    print("----------------------------")
    print(f"Customer ID       : {customer_id}")
    print(f"Customer Name     : {customer_name}")
    print(f"Units Consumed    : {units_consumed}")
    print(f"Charge per Unit   : Kshs. {charge_per_unit:.2f}")
    print(f"Total Amount to Pay: Kshs. {total_bill:.2f}")

calculate_electricity_bill()