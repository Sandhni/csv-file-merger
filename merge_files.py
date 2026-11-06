import sys
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent
input_folder = BASE_DIR / "input"
output_folder = BASE_DIR / "output"

EXPECTED_COLUMNS = ["OrderID", "Date", "Product", "Quantity", "Price"]
column_lookup = {col.lower(): col for col in EXPECTED_COLUMNS}

csv_files = sorted(input_folder.glob("*.csv"))
if not csv_files:
    sys.exit("No CSV files found in the input folder.")

dataframes = []
skipped = []

for file in csv_files:
    try:
        df = pd.read_csv(file)
    except (OSError, pd.errors.ParserError, pd.errors.EmptyDataError, UnicodeDecodeError) as error:
        print(f"Could not read {file.name}: {error}")
        skipped.append(file.name)
        continue

    # Clean column names: remove extra spaces and ignore upper/lower case
    df.columns = df.columns.str.strip()
    df = df.rename(columns=lambda c: column_lookup.get(c.lower(), c))

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        print(f"Skipped {file.name}: missing columns {sorted(missing)}")
        skipped.append(file.name)
        continue

    # Fix column order and record which file each row came from
    df = df[EXPECTED_COLUMNS].assign(SourceFile=file.name)
    dataframes.append(df)

if not dataframes:
    sys.exit("No valid CSV files could be merged.")

# Combine files and remove duplicate sales records
merged_df = pd.concat(dataframes, ignore_index=True)

rows_before = len(merged_df)
merged_df = merged_df.drop_duplicates(subset=EXPECTED_COLUMNS)
duplicates_removed = rows_before - len(merged_df)

output_folder.mkdir(exist_ok=True)
output_file = output_folder / "merged_sales.csv"
merged_df.to_csv(output_file, index=False)

print(f"Files merged: {len(dataframes)}")
print(f"Files skipped: {len(skipped)}")
print(f"Duplicate rows removed: {duplicates_removed}")
print(f"Total records saved: {len(merged_df)}")
print(f"Saved to: {output_file}")