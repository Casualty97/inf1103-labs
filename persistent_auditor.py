# INF1103 Lab 4 - Smart Inventory Auditor (Data Persistence)
# Lab 3's modular design, plus file handling and a list so the inventory and the
# transaction history survive after the program - or the container - stops.

TAX_RATE = 0.10
OVERSTOCK_LIMIT = 500
INVENTORY_FILE = "inventory.txt"


def load_inventory():
    """Read the saved state back into memory at startup.

    In:  nothing.
    Out: (total, history) - the saved running total and the list of every
         transaction recorded so far. Returns (0, []) when there is no file yet,
         which is the normal case on a first run, so it must not be an error.
    """
    try:
        file = open(INVENTORY_FILE, "r")
    except FileNotFoundError:
        print("No", INVENTORY_FILE, "found - starting with an empty inventory.")
        return 0, []

    lines = file.read().splitlines()
    file.close()

    total = 0
    if len(lines) > 0 and lines[0].strip() != "":
        total = int(lines[0].strip())

    history = []
    if len(lines) > 1 and lines[1].strip() != "":
        for amount in lines[1].split(","):
            history.append(int(amount))

    print("Loaded", INVENTORY_FILE + ":", total, "units from",
          len(history), "past transactions.")
    return total, history


def get_valid_input():
    """In: nothing. Out: an int, the string "quit", or None for a bad entry."""
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
    """In: one delivery amount. Out: the tax due on that delivery (10%)."""
    return amount * TAX_RATE


def generate_report(total_units, failed_attempts, deliveries=0):
    """Print the closing summary. Extra figures are optional parameters so the
    two-argument call required by the lab sheet still works."""
    print("===================================")
    print("AUDIT REPORT")
    print("Total Deliveries Processed:", deliveries)
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("===================================")


def main():
    # 1. Persistence: pick up where the last run left off
    inventory, history = load_inventory()

    failed_entries = 0
    deliveries = 0

    print("===================================")
    print("Smart Inventory Auditor (Persistent)")
    print("Current Inventory:", inventory, "units")
    print("Enter a stock quantity, or type 'quit' to finish.")
    print("===================================")

    while True:
        result = get_valid_input()

        if result == "quit":
            break
        elif result is None:
            failed_entries = failed_entries + 1
        else:
            inventory = process_delivery(inventory, result)
            tax = calculate_tax(result)
            deliveries = deliveries + 1

            # 2. History tracking: every valid transaction goes into the list
            history.append(result)

            print("Accepted:", result, "units | tax on this delivery:",
                  round(tax, 2), "| inventory now", inventory)

            if inventory > OVERSTOCK_LIMIT:
                print("!! OVERSTOCK ALERT: inventory has exceeded",
                      OVERSTOCK_LIMIT, "units. Stopping the audit.")
                break

    generate_report(inventory, failed_entries, deliveries)


if __name__ == "__main__":
    main()
