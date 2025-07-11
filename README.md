# CustomCrawler

CustomCrawler is a simple Python script used to discover subdomains and directories for a given URL. It scans for potential targets using a user-provided wordlist file.

## Features

-   **Subdomain Finder (`-s`):** Searches for subdomains in the format `word.domain.com` for a specified domain.
-   **Directory Finder (`-d`):** Searches for directories or files in the format `https://domain.com/word` for a specified URL.
-   **Interactive Interface:** Provides a simple and clear command-line interface.
-   **Error Handling:** Checks for basic errors like invalid file paths or URLs.

## Requirements

-   [Python 3.x](https://www.python.org/downloads/)
-   `requests` library

## Installation

1.  **Clone or download the project:**
    Download the `crawler.py` file from this repository to your computer.

2.  **Install the required library:**
    Run the following command in your terminal or command prompt to install the `requests` library:
    ```bash
    pip install requests
    ```

3.  **Create a Wordlist:**
    Create a `.txt` file containing the subdomain or directory names you want to scan for. For example, you can create a file named `wordlist.txt` and add the following content:

    ```
    admin
    api
    blog
    dev
    test
    backup
    config
    ```

## Usage

To run the script, use your terminal or command prompt:

```bash
python crawler.py
```

When the program starts, you will see a screen like this:

```
CustomCrawler
Type --help for help.
```

### Commands

-   `--help`: Lists the available commands.
    -   `-s`: Starts the subdomain finder.
    -   `-d`: Starts the directory finder.
-   `exit`: Exits the program.

### Example Usages

#### Finding Subdomains

1.  After starting the program, type `-s` and press Enter.
2.  Enter the path to your wordlist file (e.g., `wordlist.txt`).
3.  Enter the target URL without `https://` (e.g., `google.com`).

The program will try each word from the wordlist as a subdomain and print the ones that are found.

```
CustomCrawler
Type --help for help.

-s
wordlist file path: wordlist.txt
url(without https): google.com
----------> https://blog.google.com is found!
----------> https://api.google.com is found!
```

#### Finding Directories

1.  After starting the program, type `-d` and press Enter.
2.  Enter the path to your wordlist file (e.g., `wordlist.txt`).
3.  Enter the target URL without `https://` (e.g., `google.com`).

The program will append each word from the wordlist to the URL and print the valid directories/files that are found.

```
CustomCrawler
Type --help for help.

-d
wordlist file path: wordlist.txt
url(without https): google.com
----------> https://google.com/blog is found!
----------> https://google.com/test is found!
```

## Code Description

-   `getwords()`: Takes a file path from the user, reads the file, and returns each line as an element in a list.
-   `request(url)`: Sends a `GET` request to the given URL. If the request is successful (a response is received), it prints that the URL is found. In case of an error, it prints the type of the error.
-   `subdomainfinder()`: Gets the wordlist using `getwords()`, prompts the user for the target URL, formats each word as a subdomain, and sends it to the `request()` function.
-   `directoryfinder()`: Works similarly to `subdomainfinder()`, but it appends the words as a directory to the end of the URL.
-   `if __name__ == "__main__":`: This is the main loop of the program. It takes user input and calls the corresponding function.