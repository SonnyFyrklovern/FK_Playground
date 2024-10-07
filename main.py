# Analysis of email marketing data

import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# Path to the CSV file on your desktop
desktop_path = os.path.expanduser("~/Desktop")
csv_file_path = os.path.join(desktop_path, "email_marketing_data.csv") # Replace with the actual path/name of your CSV file

# Read the CSV file
data = []
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        data.append(row)

# Convert data to numpy array
data_array = np.array(data)

print("Data imported successfully!")
print(f"Number of rows: {data_array.shape[0]}")
print(f"Number of columns: {data_array.shape[1]}")
print(f"Column headers: {headers}")

# ... (Your analysis code will go here)

# The following lines should be placed at the bottom of your script, after any analysis

# Path for the new CSV file on your desktop
new_csv_file_path = os.path.join(desktop_path, "processed_email_marketing_data.csv")

# Save the data_array to a new CSV file
with open(new_csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)  # Write the headers
    csv_writer.writerows(data_array)  # Write the data

print(f"Processed data saved to: {new_csv_file_path}")
