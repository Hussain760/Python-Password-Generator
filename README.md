# Password Generator

This repository contains a Python-based password generator that allows users to specify the length and composition of passwords.

## Files

### `utils.py`

The `utils.py` file contains functions to generate random characters for passwords based on ASCII values. It includes functions for uppercase letters, lowercase letters, numbers, and symbols.

### `index.py`

The `index.py` file is the main script for the password generator. It prompts users to input the desired length and number of passwords, as well as whether they need uppercase letters, lowercase letters, numbers, or symbols in their passwords. It then generates passwords accordingly using functions from `utils.py`.

## Usage

1. **Run `index.py`:**

   - Execute `index.py` using a Python interpreter.
   - Follow the prompts to input the desired length and composition of passwords.
   - Receive generated passwords based on the provided criteria.

2. **Customization:**
   - Modify `index.py` to change the user prompts or logic for password generation.
   - Update `utils.py` to alter the character sets or methods used for generating specific types of characters.

## How to Run

Ensure you have Python installed on your system.

1. Clone the repository:

   ```bash
   git clone https://github.com/Hussain760/Python-Password-Generator.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd Python-Password-Generator
   ```

3. Run the password generator:

   ```bash
   python index.py
   ```

## Contributions

Contributions to enhance the password generator or fix any issues are welcome! Feel free to fork this repository give it a star, make changes, and submit a pull request.
