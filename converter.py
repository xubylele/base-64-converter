import argparse
import base64


def base64_file_to_pdf(input_file, output_file):
    with open(input_file, 'r') as file:
        base64_str = file.read()

    pdf_data = base64.b64decode(base64_str)

    with open(output_file, 'wb') as file:
        file.write(pdf_data)

    print(f"File converted successfully: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert a base64 encoded file to a file.')
    parser.add_argument('-i', '--input', type=str, required=True,
                        help='File with the base64 encoded data.')
    parser.add_argument('-o', '--output', type=str,
                        required=True, help='Output file.')

    args = parser.parse_args()

    base64_file_to_pdf(args.input, args.output)


if __name__ == '__main__':
    main()
