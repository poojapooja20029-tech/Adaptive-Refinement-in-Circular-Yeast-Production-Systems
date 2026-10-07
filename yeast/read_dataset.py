import csv

input_file = 'yeast/dataset/pdf1_yeast_biomass.csv'

with open(input_file, 'r') as file:

    reader = csv.DictReader(file)

    rows = list(reader)


for row in rows:

    row['experiment_no'] = int(row['experiment_no'].strip())

    row['temperature_C'] = float(row['temperature_C'].strip())

    row['pH'] = float(row['pH'].strip())

    row['sugar_g_L'] = float(row['sugar_g_L'].strip())

    row['observed_biomass_g_L'] = float(
        row['observed_biomass_g_L'].strip()
    )


print("First row after cleaning:")
print(rows[0])

print("\nChecking for extra spaces:")

for row in rows:

    for column in row:

        if isinstance(row[column], str) and row[column] != row[column].strip():
            print(column, "has extra spaces")

print("Extra space check completed.")

print("\nChecking for duplicate records:")

seen = set()
duplicates = 0

for row in rows:

    row_tuple = tuple(row.items())

    if row_tuple in seen:
        duplicates += 1

    else:
        seen.add(row_tuple)

print("Duplicate records:", duplicates)
print("\nChecking for invalid values:")

invalid_values = 0

for row in rows:

    if row['temperature_C'] < 0:
        invalid_values += 1

    if row['pH'] < 0:
        invalid_values += 1

    if row['sugar_g_L'] < 0:
        invalid_values += 1

    if row['observed_biomass_g_L'] < 0:
        invalid_values += 1


print("Invalid values:", invalid_values)
output_file = 'yeast/dataset/pdf1_yeast_biomass_cleaned.csv'

fieldnames = [
    'experiment_no',
    'temperature_C',
    'pH',
    'sugar_g_L',
    'observed_biomass_g_L'
]

with open(output_file, 'w', newline='') as file:

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(rows)

print("\nCleaned dataset saved successfully.")
print("File:", output_file)