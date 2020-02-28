INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

reader = open("input.txt")
writer = open("output.txt", "w")
for line in reader:
    transformed_line = line.upper()
    writer.write(transformed_line)

reader.close()
writer.close()