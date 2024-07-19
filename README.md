# Welcome

## This is an application that allows you to convert base64 encoded strings to converted files

### Why is this project necessary?

In many cases, sensitive information needs to be shared or stored in a secure manner. By converting files to a base64 string, the data can be encapsulated and transmitted as plain text, ensuring that it remains intact and unaltered during transit. This project allows you to convert those base64 encoded strings back into their original format, ensuring the privacy and integrity of the data.

### How to use it?

1. Run the installation command: ```pip install -r requirements.txt```

2. You can run the application by running the command: ``` python converter.py --input fileToConvert.txt --output output.format ```

### Command line arguments

- -i, --input: The path to the file that contains the base64 string you want to convert to any file format.
- -o, --output: The path where you want to save the converted file. Is required when converting from base64 to a file format.
- h, --help: Show the help message and exit.
- -m, --mode: The mode of the conversion. It can be either "to_base64" or "from_base64". The default mode is "from_base64".

### Example

- Create a text file (e.g., fileToConvert.txt) that contains the base64 string.
- Run the conversion command:
  
  ```bash
    python converter.py --input fileToConvert.txt --output output.pdf --mode from_base64
  ```
