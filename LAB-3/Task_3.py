def get_customer_details():
    """Function to collect customer details"""
    print("Customer Details Collection")
    print("-" * 30)
    
    customer_details = {}
    
    # Get customer name
    while True:
        name = input("Enter customer name: ").strip()
        if name:
            customer_details['name'] = name
            break
        else:
            print("Name cannot be empty. Please enter a valid name.")
    
    # Get customer address
    while True:
        address = input("Enter customer address: ").strip()
        if address:
            customer_details['address'] = address
            break
        else:
            print("Address cannot be empty. Please enter a valid address.")
    
    # Get phone number
    while True:
        phone = input("Enter phone number: ").strip()
        if phone and phone.replace('-', '').replace(' ', '').isdigit():
            customer_details['phone'] = phone
            break
        else:
            print("Please enter a valid phone number.")
    
    # Get customer ID
    while True:
        customer_id = input("Enter customer ID: ").strip()
        if customer_id:
            customer_details['customer_id'] = customer_id
            break
        else:
            print("Customer ID cannot be empty. Please enter a valid ID.")
    
    # Get email (optional)
    email = input("Enter email address (optional): ").strip()
    if email:
        customer_details['email'] = email
    
    print("\nCustomer Details Collected Successfully!")
    print("-" * 30)
    return customer_details

def calculate_power_bill():
    print("Power Bill Calculator")
    print("=" * 50)
    
    # Get customer details first
    customer = get_customer_details()
    
    print("\nNow let's calculate your power bill...")
    print("-" * 30)
    
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for units.")
        return

    # Example slab rates (customize as needed)
    # First 100 units: Rs. 5 per unit
    # Next 100 units (101-200): Rs. 7 per unit
    # Above 200 units: Rs. 10 per unit
    bill = 0.0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    # Display bill with customer details
    print("\n" + "=" * 50)
    print("POWER BILL STATEMENT")
    print("=" * 50)
    print(f"Customer Name: {customer['name']}")
    print(f"Customer ID: {customer['customer_id']}")
    print(f"Address: {customer['address']}")
    print(f"Phone: {customer['phone']}")
    if 'email' in customer:
        print(f"Email: {customer['email']}")
    print("-" * 50)
    print(f"Total units consumed: {units}")
    print(f"Total power bill: Rs. {bill:.2f}")
    print("=" * 50)

def show_previous_bill_details():
    """Function to display previous bill details"""
    print("\nPrevious Bill Details")
    print("=" * 50)
    
    # Sample previous bill data (in a real application, this would come from a database)
    previous_bills = [
        {
            'bill_date': '2024-01-15',
            'customer_name': 'John Doe',
            'customer_id': 'CUST001',
            'units_consumed': 150,
            'bill_amount': 950.00,
            'payment_status': 'Paid'
        },
        {
            'bill_date': '2024-02-15',
            'customer_name': 'John Doe',
            'customer_id': 'CUST001',
            'units_consumed': 180,
            'bill_amount': 1160.00,
            'payment_status': 'Paid'
        },
        {
            'bill_date': '2024-03-15',
            'customer_name': 'John Doe',
            'customer_id': 'CUST001',
            'units_consumed': 120,
            'bill_amount': 740.00,
            'payment_status': 'Unpaid'
        }
    ]
    
    if not previous_bills:
        print("No previous bill records found.")
        return
    
    print(f"Found {len(previous_bills)} previous bill(s):")
    print("-" * 50)
    
    for i, bill in enumerate(previous_bills, 1):
        print(f"Bill #{i}")
        print(f"  Date: {bill['bill_date']}")
        print(f"  Customer: {bill['customer_name']} (ID: {bill['customer_id']})")
        print(f"  Units Consumed: {bill['units_consumed']}")
        print(f"  Bill Amount: Rs. {bill['bill_amount']:.2f}")
        print(f"  Status: {bill['payment_status']}")
        print("-" * 50)
    
    # Calculate summary statistics
    total_bills = len(previous_bills)
    total_amount = sum(bill['bill_amount'] for bill in previous_bills)
    total_units = sum(bill['units_consumed'] for bill in previous_bills)
    paid_bills = sum(1 for bill in previous_bills if bill['payment_status'] == 'Paid')
    unpaid_bills = total_bills - paid_bills
    
    print("\nSUMMARY STATISTICS:")
    print("-" * 30)
    print(f"Total Bills: {total_bills}")
    print(f"Total Amount: Rs. {total_amount:.2f}")
    print(f"Total Units: {total_units}")
    print(f"Paid Bills: {paid_bills}")
    print(f"Unpaid Bills: {unpaid_bills}")
    print(f"Average Bill: Rs. {total_amount/total_bills:.2f}")
    print("=" * 50)

def main_menu():
    """Main menu function"""
    while True:
        print("\n" + "=" * 50)
        print("POWER BILL MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Calculate New Power Bill")
        print("2. View Previous Bill Details")
        print("3. Exit")
        print("-" * 50)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            calculate_power_bill()
        elif choice == '2':
            show_previous_bill_details()
        elif choice == '3':
            print("Thank you for using the Power Bill Management System!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()