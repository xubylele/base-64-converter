import argparse
import base64


def base64_to_file(input_file, output_file=None):
    if not output_file:
        print('Output file is required for this mode.')
        return

    with open(input_file, 'r') as file:
        base64_str = file.read()

    file_data = base64.b64decode(base64_str)

    with open(output_file, 'wb') as file:
        file.write(file_data)
    print(f"File converted successfully: {output_file}")


def file_to_base64(input_file, output_file=None):
    with open(input_file, 'rb') as file:
        file_data = file.read()

    base64_str = base64.b64encode(file_data).decode('utf-8')

    if output_file:
        with open(output_file, 'w') as file:
            file.write(base64_str)
        print(f"File converted successfully: {output_file}")
    else:
        print(base64_str)


def main():
    parser = argparse.ArgumentParser(
        description='Convert a file to/from base64.')
    parser.add_argument('-i', '--input', type=str, required=True,
                        help='Input file.')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file (optional).')
    parser.add_argument('-m', '--mode', type=str, required=True, choices=['to_base64', 'from_base64'],
                        help='Conversion mode: "to_base64" or "from_base64".')

    args = parser.parse_args()

    if args.mode == 'to_base64':
        file_to_base64(args.input, args.output)
    elif args.mode == 'from_base64':
        base64_to_file(args.input, args.output)


if __name__ == '__main__':
    main()
