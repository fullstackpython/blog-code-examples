import os


def lambda_handler(event, context):
    what_to_print = os.environ.get("what_to_print")
    how_many_times = int(os.environ.get("how_many_times"))

    # make sure what_to_print and how_many_times values exist
    if what_to_print and how_many_times > 0:
        for i in range(0, how_many_times):
            print(what_to_print)
        return what_to_print
    return None
