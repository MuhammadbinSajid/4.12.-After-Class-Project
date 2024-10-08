# Function to calculate due amount
def calculate_due_amount(total_bill, amount_paid):
    if amount_paid > total_bill:
        return "The payment exceeds the bill amount."
    due_amount = total_bill - amount_paid
    return due_amount

# Input from the user
total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

# Calculate and display the due amount
due_amount = calculate_due_amount(total_bill, amount_paid)
print(f"The remaining due amount is: {due_amount}")
