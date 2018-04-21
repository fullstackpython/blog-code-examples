import os
import rollbar


ROLLBAR_KEY = os.getenv('ROLLBAR_SECRET_KEY', 'missing Rollbar secret key')
rollbar.init(ROLLBAR_KEY, 'production')


@rollbar.lambda_function
def lambda_handler(event, context):
    what_to_print = os.environ.get("what_to_print")
    how_many_times = int(os.environ.get("how_many_times"))

    # make sure what_to_print and how_many_times values exist
    if what_to_print and how_many_times > 0:
        for i in range(0, how_many_times):
            # formatted string literals are new in Python 3.6
            print(f"what_to_print: {what_to_print}.")
        return what_to_print
    return None
