helpers_content = '''def validate_input(prompt, valid_type=str, condition=lambda x: True, error_message="Invalid input"):
    while True:
        try:
            value = valid_type(input(prompt))
            if not condition(value):
                raise ValueError()
            return value
        except ValueError:
            print(error_message)
'''