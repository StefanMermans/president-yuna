import argparse
from typing import List
from random import randrange
from datetime import datetime

SERVER_RESET = 10


def get_from_list(text_list: List[str]) -> str:
    return text_list[randrange(len(text_list))]


def get_early_text(remaining_time):
    early_texts = [
        "We're going to have a war today, make sure to participate ok? There's {} left",
    ]
    return get_from_list(early_texts).format(str(remaining_time))


def get_late_text(remaining_time):
    late_texts = [
        "Make sure to do your attacks in time before the war ends in {}"
    ]
    return get_from_list(late_texts).format(str(remaining_time))


def get_remaining_time() -> str:
    now = datetime.utcnow()

    if now.hour > 10:
        # First day
        remaining_hours = 10 + (23 - now.hour)
    else:
        # Second day
        remaining_hours = 10 - now.hour

    return "{} hours".format(remaining_hours)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, choices=["early", "late"], required=True)
    return parser.parse_args()


def get_message():
    args = get_parser()
    type_args = args.type
    remaining_time = get_remaining_time()

    if type_args == "early":
        return get_early_text(remaining_time)
    elif type_args == "late":
        return get_late_text(remaining_time)

    raise KeyError("invalid type argument!")
