# INF1103 Lab 2 - Smart Inventory Auditor
# Flow control: conditional statements (if / elif / else) and a while loop.

# 1. Initialize the inventory to zero in the start
inventory = 0
failed_entries = 0

print("===================================")
print("Smart Inventory Auditor")
print("Enter a stock quantity, or type 'quit' to finish.")
print("===================================")

# 2. Run in a continuous loop until the user types quit.
#    A while loop is the right choice here: we do not know in advance how many
#    deliveries the operator will key in, so there is nothing to count through
#    with a for loop. We just keep going until a condition tells us to stop.
while True:
    entry = input("Enter stock quantity: ")

    if entry.lower() == "quit":
        break

    # 3. Accept stock values as integers.
    #    .isdigit() is only True for a run of digits, so it rejects "ten" for us.
    elif entry.isdigit():
        quantity = int(entry)

        # 6. Manage state: keep a running total of the inventory.
        inventory = inventory + quantity
        print("Accepted:", quantity, "units. Inventory is now", inventory, "units.")

        # 7. Trigger the overstock alert and stop auditing immediately.
        if inventory > 500:
            print("!! OVERSTOCK ALERT: inventory has exceeded 500 units. Stopping the audit.")
            break

    # 5. Enforce business rules: reject negative numbers.
    #    "-5".isdigit() is False, so a negative value would otherwise be reported
    #    as "not a number". Checking for a leading minus sign keeps the two
    #    business rules separate and gives the operator a useful message.
    elif entry.startswith("-") and entry[1:].isdigit():
        print("Rejected: negative quantities are not allowed.")
        failed_entries = failed_entries + 1

    # 4. Handle invalid input: anything else is dirty data. Print an error and
    #    carry on with the next iteration instead of crashing.
    else:
        print("Rejected: '" + entry + "' is not a whole number.")
        failed_entries = failed_entries + 1

# 8. Reporting
print("===================================")
print("AUDIT REPORT")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)
print("===================================")
