from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
input_folder = BASE_DIR / "input"

input_folder.mkdir(exist_ok=True)

# Create 10 CSV files with 300 records each
for file_number in range(1, 11):
    start_id = (file_number - 1) * 300 + 1

    df = pd.DataFrame({
        "OrderID": range(start_id, start_id + 300),
        "Date": ["2026-01-15"] * 300,
        "Product": ["Keyboard", "Mouse", "Monitor"] * 100,
        "Quantity": [1, 2, 3] * 100,
        "Price": [750, 400, 8500] * 100
    })

    # Change column order in file 2
    if file_number == 2:
        df = df[["Product", "OrderID", "Price", "Date", "Quantity"]]

    # Add extra spaces and different capitalization in file 3
    if file_number == 3:
        df.columns = [" orderid ", "DATE", " Product ", "quantity", "PRICE"]

    # Add duplicate records to file 4
    if file_number == 4:
        df.iloc[0:5].to_csv(
            input_folder / "duplicate_rows.csv",
            index=False
        )

    df.to_csv(
        input_folder / f"sales_{file_number:02}.csv",
        index=False
    )

# Create an invalid CSV missing the Price column
invalid_df = pd.DataFrame({
    "OrderID": [90001, 90002],
    "Date": ["2026-04-01", "2026-04-02"],
    "Product": ["Keyboard", "Mouse"],
    "Quantity": [1, 2]
})
invalid_df.to_csv(input_folder / "invalid_sales.csv", index=False)

# Create an unrelated non-CSV file
(input_folder / "notes.txt").write_text(
    "This file should be ignored by the merger.",
    encoding="utf-8"
)

print("Test data created successfully.")
print("Created 10 sales CSV files, one invalid CSV, and one text file.")
