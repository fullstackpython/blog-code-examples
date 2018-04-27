import os
import rollbar


ROLLBAR_KEY = os.getenv('ROLLBAR_SECRET_KEY', 'missing Rollbar secret key')
rollbar.init(ROLLBAR_KEY, 'production')


@rollbar.lambda_function
def lambda_handler(event, context):
    message = os.getenv("message")
    print_count = int(os.getenv("print_count"))

    # check if message exists and how many times to print it
    if message and print_count > 0:
        for i in range(0, print_count):
            # formatted string literals are new in Python 3.6
            print(f"message: {message}.")
        return print_count
    return None
