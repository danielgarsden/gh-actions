class UpperCaseConverter:
    def __init__(self, input_string: str):
        self.input_string = input_string

    def to_upper(self) -> str:
        return self.input_string.upper()


if __name__ == '__main__':
    import sys
    # Check if a command line argument was provided; if not, prompt the user for input
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = input("Enter a string: ")

    converter = UpperCaseConverter(text)
    result = converter.to_upper()
    print(result)