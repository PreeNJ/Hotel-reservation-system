# lib/helpers.py

def validate_input(prompt, valid_type=str, condition=lambda x: True, error_message="Invalid input"):
    """
    Repeatedly prompt the user until they enter something that:
      • Can be converted to `valid_type` (e.g. int, float, etc.)
      • Satisfies the `condition(value)` check (default always True)
    Returns the validated, cast value.
    """
    while True:
        try:
            value = valid_type(input(prompt))
            if not condition(value):
                raise ValueError()
            return value
        except ValueError:
            print(error_message)
