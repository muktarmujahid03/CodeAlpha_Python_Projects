import csv

# Sample prices for this programming project
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 170.00,
    "AMZN": 190.00
}

def main():
    portfolio = []
    total_value = 0.0

    print("\n=== STOCK PORTFOLIO TRACKER ===")
    print("Available sample stocks:", ", ".join(STOCK_PRICES))

    while True:
        symbol = input("\nEnter a stock symbol (or DONE to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("That symbol is not in the sample price list.")
            continue

        try:
            quantity = int(input(f"How many shares of {symbol}? "))

            if quantity <= 0:
                print("Quantity must be positive.")
                continue

        except ValueError:
            print("Please enter a whole number.")
            continue

        price = STOCK_PRICES[symbol]
        investment = price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        total_value += investment

        print(f"Added {quantity} share(s) of {symbol}: ${investment:,.2f}")

    print("\n=== PORTFOLIO SUMMARY ===")

    if not portfolio:
        print("No stocks were added.")
        return

    for item in portfolio:
        print(
            f'{item["symbol"]}: {item["quantity"]} share(s) '
            f'x ${item["price"]:,.2f} = ${item["investment"]:,.2f}'
        )

    print(f"\nTotal investment value: ${total_value:,.2f}")

    save = input("Save this result to portfolio.csv? (y/n): ").strip().lower()

    if save == "y":
        with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["symbol", "quantity", "price", "investment"]
            )
            writer.writeheader()
            writer.writerows(portfolio)

        print("Saved successfully as portfolio.csv.")

if __name__ == "__main__":
    main()
