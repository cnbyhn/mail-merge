# mail-merge
Developed a Python script that automates the creation of personalized letters by reading recipient names from a file, generating custom content based on a template, and saving the output to a specified directory.
# Personalized Letter Generator

## Description
The Personalized Letter Generator is a Python script that automates the creation of personalized letters. It reads a list of recipient names from a file, generates a letter for each recipient using a predefined template, and saves the output letters in a specified directory.

## Features
- **Personalized Content**: Each letter is customized with the recipient's name.
- **Batch Processing**: Automatically processes multiple recipients at once by reading from a text file.
- **Output Management**: Saves the generated letters to an output directory for easy access.

## Requirements
- Python 3.x

## Setup
1. **Prepare Input File**: Create a text file with the names of recipients, one name per line.
2. **Prepare Letter Template**: Ensure the template contains a placeholder for the recipient’s name.
3. **Run the Script**:
   - Place your recipient names in a text file (`invited_names.txt`).
   - Run the `main.py` script:
     ```bash
     python main.py
     ```

4. The script will generate personalized letters and save them in the `output_letters` directory.

## Usage
- **Input File**: Contains the names of recipients.
- **Template File**: Contains the format of the letter with placeholders.
- **Output**: The personalized letters are saved in the `output_letters` directory.

## Notes
- Ensure that the input file (`invited_names.txt`) is in the same directory as the script.
- The output directory (`output_letters`) will be automatically created to store the generated letters.

To run the project:
```bash
python main.py

