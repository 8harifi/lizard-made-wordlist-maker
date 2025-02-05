

---

# wordlist_maker

## Usage

Generate custom wordlists with various configurations for use in dictionary attacks, including WPA and WPA2 WiFi passwords.

### Options:

- `--wpa`, `-w`  
  Generate a password list for WPA and WPA2 WiFi networks (includes both capital and lowercase letters by default).

- `--capital`, `-c`  
  May include capital letters.

- `--no-capital`  
  Excludes capital letters.

- `--need-capital`  
  Requires capital letters.

- `--small`, `-s`  
  May include lowercase letters.

- `--no-small`  
  Excludes lowercase letters.

- `--need-small`  
  Requires lowercase letters.

- `--number`, `-n`  
  May include numbers.

- `--no-number`  
  Excludes numbers.

- `--need-number`  
  Requires numbers.

- `--input`, `-i`  
  Path to a file containing raw words.

- `--output`, `-o`  
  Path to the output file.

- `--length-at-least`  
  Specifies the minimum allowed password length.

- `--length-at-most`  
  Specifies the maximum allowed password length.

- `--best-performance`, `-b`  
  Best performance mode; provides fewer words with a lower probability of a successful attack.

- `--most-probable`, `-m`  
  Most probable mode; generates more words with a higher probability of a successful attack.

### Default Configuration:
```
--small-needed --number-needed --capital --length-at-least 0 --length-at-most 100 -o wordlist_output.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/8harifi/wordlist_maker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd wordlist_maker/
   ```

3. Install the module:
   ```bash
   python3 setup.py install
   ```

4. Verify installation:
   ```bash
   wordlist_maker --help
   ```

---

## Features:

- **Speed:** This tool is optimized for fast performance.
- **Customization:** You can generate wordlists with specific rules (e.g., length, characters, and types of characters).
- **Exclusion of Unwanted Words:** It will automatically remove passwords that don't meet your specified criteria, such as those with only numbers or without any capital letters.

This tool is ideal for dictionary-based WiFi handshake attacks, ensuring that only relevant password candidates are included in your wordlist.

---

## License

[MIT](https://github.com/8harifi/wordlist_maker/blob/main/LICENSE)

