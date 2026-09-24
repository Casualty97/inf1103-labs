# INF1103 Lab 3 - Smart Inventory Auditor (Modular Design)
# Same behaviour as Lab 2, but the logic now lives in functions.
#
# Function signatures mapped out before writing any code:
#   get_valid_input()                          -> int | "quit" | None
#   process_delivery(current_total, new_value) -> int   (the new running total)
#   calculate_tax(amount)                      -> float (10% of that delivery)
#   generate_report(total_units, failed_attempts) -> None (prints the summary)

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
            # 3. A valid value: update the total and the counters
            inventory = inventory + result
            deliveries = deliveries + 1

            print("Accepted:", result, "units. Inventory is now", inventory, "units.")

            if inventory > OVERSTOCK_LIMIT:
                print("!! OVERSTOCK ALERT: inventory has exceeded",
                      OVERSTOCK_LIMIT, "units. Stopping the audit.")
                break

    # 4. Reporting
    print("===================================")
    print("AUDIT REPORT")
    print("Total Deliveries Processed:", deliveries)
    print("Total Units Processed:", inventory)
    print("Number of Failed/Rejected Entries:", failed_entries)
    print("===================================")


if __name__ == "__main__":
    main()
