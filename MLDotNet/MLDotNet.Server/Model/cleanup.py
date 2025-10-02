input_file = "customer_support_tickets - Copy.csv"
output_file = "cleaned.csv"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        # Keep only rows that aren’t empty or just commas
        if line.strip() and not all(ch == "," for ch in line.strip()):
            outfile.write(line)

print(f"Cleaned file saved as {output_file}")
