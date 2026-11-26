
import csv
import os

# --------------------------------
# FILE PATHS
# --------------------------------

INPUT_FILE = "stocks.csv"
OUTPUT_FILE = "portfolio_summary.csv"


# --------------------------------
# READ STOCK DATA
# --------------------------------

portfolio = {}

try:
    with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.DictReader(file)

        # Clean CSV column names
        if reader.fieldnames:
            reader.fieldnames = [
                name.strip().replace("\ufeff", "")
                for name in reader.fieldnames
            ]

        # Required columns
        required_columns = [
            "Ticker",
            "Buy_Price",
            "Current_Price",
            "Quantity"
        ]

        if not reader.fieldnames:
            raise ValueError("stocks.csv is empty!")

        for column in required_columns:
            if column not in reader.fieldnames:
                raise ValueError(
                    f"Missing column: {column}. "
                    f"Available columns: {reader.fieldnames}"
                )

        # Read each stock
        for row in reader:

            ticker = row["Ticker"].strip().upper()

            if ticker == "":
                continue

            buy_price = float(row["Buy_Price"])
            current_price = float(row["Current_Price"])
            quantity = int(row["Quantity"])

            portfolio[ticker] = {
                "buy_price": buy_price,
                "current_price": current_price,
                "quantity": quantity
            }


except FileNotFoundError:
    print("Error: stocks.csv file not found!")
    print("Create stocks.csv in the same folder.")
    exit()

except ValueError as error:
    print("CSV Error:", error)
    exit()


# --------------------------------
# CALCULATE PORTFOLIO
# --------------------------------

total_investment = 0
total_current_value = 0

print("\n========================================")
print("       STOCK PORTFOLIO TRACKER")
print("========================================")

print(
    f"{'Stock':<12}"
    f"{'Invested':<15}"
    f"{'Current':<15}"
    f"{'Gain/Loss %':<15}"
)

print("-" * 57)

for ticker, details in portfolio.items():

    buy_price = details["buy_price"]
    current_price = details["current_price"]
    quantity = details["quantity"]

    invested = buy_price * quantity
    current_value = current_price * quantity

    gain_loss = current_value - invested

    if invested != 0:
        percentage = (gain_loss / invested) * 100
    else:
        percentage = 0

    total_investment += invested
    total_current_value += current_value

    print(
        f"{ticker:<12}"
        f"₹{invested:<14.2f}"
        f"₹{current_value:<14.2f}"
        f"{percentage:.2f}%"
    )


# --------------------------------
# TOTAL PROFIT OR LOSS
# --------------------------------

total_gain_loss = total_current_value - total_investment

if total_investment != 0:
    total_percentage = (
        total_gain_loss / total_investment
    ) * 100
else:
    total_percentage = 0

print("-" * 57)

print("\nTotal Investment     :", f"₹{total_investment:.2f}")
print("Current Portfolio    :", f"₹{total_current_value:.2f}")
print("Total Gain/Loss      :", f"₹{total_gain_loss:.2f}")
print("Overall Gain/Loss %  :", f"{total_percentage:.2f}%")


# --------------------------------
# AUTOMATIC CSV FILE CREATION
# --------------------------------

try:
    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Total Investment",
            "Current Portfolio Value",
            "Total Gain/Loss",
            "Gain/Loss Percentage"
        ])

        writer.writerow([
            total_investment,
            total_current_value,
            total_gain_loss,
            total_percentage
        ])

    print("\nSUCCESS! Summary CSV created.")
    print("File location:", os.path.abspath(OUTPUT_FILE))

except OSError as error:
    print("Unable to create CSV file:", error)
