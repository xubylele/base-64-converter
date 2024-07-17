import argparse
import base64


def base64_file_to_pdf(input_file, output_file):
    with open(input_file, 'r') as file:
        base64_str = file.read()

    pdf_data = base64.b64decode(base64_str)

    with open(output_file, 'wb') as file:
        file.write(pdf_data)


def main():
    parser = argparse.ArgumentParser(
        description='Convert a base64 encoded file to a PDF file.')
    parser.add_argument('--input', type=str, required=True,
                        help='File with the base64 encoded data.')
    parser.add_argument('--output', type=str, required=True,
                        help='Output PDF file.')

    args = parser.parse_args()

    base64_file_to_pdf(args.input, args.output)


if __name__ == '__main__':
    main()
