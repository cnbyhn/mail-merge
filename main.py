
import os

# Ensure output directory exists
output_dir = "ReadyToSend"
os.makedirs(output_dir, exist_ok=True)

# Load names and template
with open("invited_names.txt") as names_file:
    names = [name.strip() for name in names_file.readlines()]

with open("starting_letter.txt") as template_file:
    template = template_file.read()

# Generate personalized letters
for name in names:
    personalized_letter = template.replace("[name]", name)
    filename = f"{output_dir}/letter_for_{name}.txt"
    with open(filename, "w") as output_file:
        output_file.write(personalized_letter)
    print(f"Letter created for {name}: {filename}")
