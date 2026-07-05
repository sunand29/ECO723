import csv
import datetime

input_file = "Series.csv"
output_file = "cleaned_data.csv"

start_date = datetime.datetime(2004, 1, 1)
end_date = datetime.datetime(2018, 12, 31)

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    header = next(reader)
    # The first column name is empty or has a BOM
    header[0] = "Date"
    writer.writerow(header)
    
    data_started = False
    for row in reader:
        # Check if the row starts with a date like "MM/YYYY"
        if len(row) > 0 and "/" in row[0] and len(row[0]) == 7:
            try:
                month, year = map(int, row[0].split('/'))
                current_date = datetime.datetime(year, month, 1)
                data_started = True
                
                # Check if it falls within our range
                if start_date <= current_date <= end_date:
                    writer.writerow(row)
            except ValueError:
                # If parsing fails, skip
                pass

print(f"Successfully cleaned data and saved to {output_file}!")
