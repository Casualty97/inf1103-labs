# INF1103 Lab 3 - Smart Inventory Auditor (Modular Design)
# Same behaviour as Lab 2, but the logic now lives in functions.
#
# Function signatures mapped out before writing any code:
#   get_valid_input()                          -> int | "quit" | None
#   process_delivery(current_total, new_value) -> int   (the new running total)
#   calculate_tax(amount)                      -> float (10% of that delivery)
#   generate_report(total_units, failed_attempts) -> None (prints the summary)

TAX_RATE = 0.10
OVERSTOCK_LIMIT = 500


def get_valid_input():
    """Prompt the operator once and validate what came back.

    In:  nothing.
    Out: the quantity as an int when the entry is usable,
         the string "quit" when the operator wants to stop,
         or None when the entry was rejected (the caller counts the failure).
    """
    entry = input("Enter stock quantity: ")

    if entry.lower() == "quit":
        return "quit"
    elif entry.isdigit():
        return int(entry)
    elif entry.startswith("-") and entry[1:].isdigit():
        print("Rejected: negative quantities are not allowed.")
        return None
    else:
        print("Rejected: '" + entry + "' is not a whole number.")
        return None


def process_delivery(current_total, new_value):
    """In: the running total and one delivery. Out: the new running total."""
    return current_total + new_value


def calculate_tax(amount):
    """In: one delivery amount. Out: the tax due on that delivery (10%).

    Note this only returns the number - it deliberately does not print it.
    """
    return amount * TAX_RATE


def generate_report(total_units, failed_attempts, deliveries=0):
    """Print the closing summary.

    The lab sheet fixes the signature as generate_report(total_units,
    failed_attempts) but also asks the report to show the delivery count, so the
    two extra figures are optional parameters. Called with just two arguments the
    function still works exactly as specified.
    """
    print("===================================")
    print("AUDIT REPORT")
    print("Total Deliveries Processed:", deliveries)
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("===================================")


def main():
    # 1. Initialize the inventory to zero in the start
    inventory = 0
    failed_entries = 0
    deliveries = 0

    print("===================================")
    print("Smart Inventory Auditor (Modular)")
    print("Enter a stock quantity, or type 'quit' to finish.")
    print("===================================")

    # 2. Run in a continuous loop until the user types quit
    while True:
        result = get_valid_input()

        if result == "quit":
            break
        elif result is None:
            failed_entries = failed_entries + 1
        else:
            # 3. A valid value: update the total, the tax and the counters
            inventory = process_delivery(inventory, result)
            tax = calculate_tax(result)
            deliveries = deliveries + 1

            print("Accepted:", result, "units | tax on this delivery:",
                  round(tax, 2), "| inventory now", inventory)

            if inventory > OVERSTOCK_LIMIT:
                print("!! OVERSTOCK ALERT: inventory has exceeded",
                      OVERSTOCK_LIMIT, "units. Stopping the audit.")
                break

    # 4. Reporting
    generate_report(inventory, failed_entries, deliveries)


if __name__ == "__main__":
    main()

# 4. Self-Reflection Task
# "Why is it better to have a calculate_tax function that simply returns a value,
#  rather than having it print the tax amount directly inside the function?"
#
# Because returning a value keeps the calculation separate from what we do with
# it. calculate_tax() answers one question - "how much tax is due on this
# amount?" - and the caller decides whether to print it, add it to a total, or
# write it to a file. If the function printed instead, the number would only ever
# exist on screen: main() could not accumulate total_tax, and the moment the
# manager asks for the tax in a file we would have to rewrite the function and
# retest everything that already depends on it. A function that returns is also
# far easier to test, because you can compare its return value against an
# expected number without capturing console output.
