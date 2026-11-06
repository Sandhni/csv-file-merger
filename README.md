# CSV File Merger

A Python automation tool that combines multiple sales CSV files into one organized dataset using Pandas.

## Features

- Automatically finds CSV files in the input folder.
- Merges multiple CSV files into a single dataset.
- Standardizes column names by handling capitalization and extra spaces.
- Arranges required columns in a consistent order.
- Skips files that cannot be read or are missing required columns.
- Removes duplicate sales records based on selected business columns.
- Tracks the original filename of each record using the `SourceFile` column.
- Saves the merged dataset as a CSV file.
- Displays a summary of processed files and records.

## Technologies Used

- Python
- Pandas
- pathlib

## Project Structure

```text
Project-2-CSV-Merger/
├── input/
│   └── CSV files to merge
├── output/
│   └── merged_sales.csv
├── merge_files.py
├── generate_test_data.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11 or compatible Python version
- Pandas

Install the required library:

```bash
pip install -r requirements.txt
```

## How to Run

1. Place the CSV files you want to merge inside the `input` folder.
2. Open a terminal in the project directory.
3. Run the script:

```bash
python merge_files.py
```

4. Find the merged output at:

```text
output/merged_sales.csv
```

## Input Data Format

The input CSV files must contain these required columns:

- `OrderID`
- `Date`
- `Product`
- `Quantity`
- `Price`

Column order, capitalization, and leading or trailing spaces in column names can differ. Files missing required columns are skipped.

## Testing

The project includes `generate_test_data.py`, which creates synthetic sales data for testing.

The test dataset includes:
- 10 sales CSV files with 300 records each.
- A separate file containing 5 records duplicated from one of the sales files.
- An invalid CSV missing the required `Price` column.
- A text file that should be ignored by the merger.

### Test Results

| Metric | Result |
|---|---:|
| Valid CSV files merged | 11 |
| CSV files skipped | 1 |
| Duplicate records removed | 5 |
| Final records saved | 3,000 |

The invalid CSV was skipped because it was missing the `Price` column. The duplicate records were identified across files and removed.

These results are from the generated test dataset; they are not results from an external client dataset.

## Duplicate Handling

Duplicate records are identified using the `OrderID`, `Date`, `Product`, `Quantity`, and `Price` columns. The first occurrence is retained, and subsequent matching records are removed.

For real-world datasets, the duplicate identification rule should be confirmed before removing records.

## Future Improvements

- Validate data types and missing values.
- Add configurable input and output file paths.
- Generate a detailed processing log.
- Add automated tests for different CSV formats and edge cases.
