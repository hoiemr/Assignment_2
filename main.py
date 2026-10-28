"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""
# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45

# ---- FUNCTIONS: replace each return 0 ----
def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR

def cost_per_month(annual_cost):
    """Give back the cost of one month of the academic year."""
    return annual_cost / MONTHS_PER_YEAR

def cost_per_day(annual_cost):
    """Give back the cost of one class day."""
    total_class_days = CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR
    return annual_cost / total_class_days

def cost_per_credit(annual_cost, credits):
    """Give back the cost of one credit this semester."""
    semester_cost = cost_per_semester(annual_cost)
    return semester_cost / credits

def cost_per_class(annual_cost, credits):
    """Give back the cost of one CS 1430 class meeting."""
    one_credit = cost_per_credit(annual_cost, credits)
    class_share = one_credit * CS1430_CREDITS
    return class_share / CS1430_MEETINGS_PER_SEMESTER

def cost_of_skipped_classes(annual_cost, credits, classes_skipped):
    """Give back the total cost of skipped CS 1430 meetings."""
    one_meeting = cost_per_class(annual_cost, credits)
    return one_meeting * classes_skipped

# ---- PROGRAM ----
def main():
    print("THE COST OF COLLEGE")
    print()
    annual_cost = float(input("Total cost for one year: "))
    credits = int(input("Credits this semester: "))
    print()

    while True:
        print("   1  Per semester")
        print("   2  Per month")
        print("   3  Per class day")
        print("   4  Per credit")
        print("   5  Per CS 1430 class")
        print("   6  Cost of skipped classes")
        print("   Q  Quit")
        print()
        choice = input("Choose an option: ").strip().upper()

        if choice == "1":
            amount = cost_per_semester(annual_cost)
            print(f"One semester costs ${amount:,.2f}")
        elif choice == "2":
            amount = cost_per_month(annual_cost)
            print(f"One month costs ${amount:,.2f}")
        elif choice == "3":
            amount = cost_per_day(annual_cost)
            print(f"One class day costs ${amount:,.2f}")
        elif choice == "4":
            amount = cost_per_credit(annual_cost, credits)
            print(f"One credit costs ${amount:,.2f}")
        elif choice == "5":
            amount = cost_per_class(annual_cost, credits)
            print(f"Every CS 1430 class costs ${amount:,.2f}")
        elif choice == "6":
            skipped = int(input("How many CS 1430 classes did you skip? "))
            amount = cost_of_skipped_classes(annual_cost, credits, skipped)
            print(f"Skipping {skipped} classes costs you ${amount:,.2f}")
        elif choice == "Q":
            print("Thanks for running the numbers!")
            break
        else:
            print("Please choose 1-6 or Q.")

        print()

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
