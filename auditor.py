# INF1103 Lab 2 - Smart Inventory Auditor
# Flow control: conditional statements (if / elif / else) and a while loop.

# 1. Initialize the inventory to zero in the start
inventory = 0

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

    print("You entered:", entry)
