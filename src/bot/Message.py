import argparse
from typing import List
from random import randrange
from datetime import datetime

SERVER_RESET = 10
PATCH_DAYS = [
    2,
    3
]


def get_from_list(text_list: List[str]) -> str:
    return text_list[randrange(len(text_list))]


def get_early_text(remaining_time):
    early_texts = [
        "@everyone There's guild war today, make sure to participate ok? There's {} left!",
        "@everyone Guild war has started, there's {} left, make sure to use your attacks!",
        "@everyone Let's win this guild war everyone! There's still {} left.",
        "@everyone Make sure to use all your attacks for the current guild war! we still have {}",
    ]
    return get_from_list(early_texts).format(str(remaining_time))


def get_late_text(remaining_time):
    late_texts = [
        "@everyone Make sure to do your attacks in time before guild war ends in {}!",
        "@everyone There's still {} left in the guild war, make sure to attack before it ends!",
        "@everyone Keep fighting, we still have {} left for the guild war!",
    ]
    return get_from_list(late_texts).format(str(remaining_time))


def get_remaining_time() -> str:
    now = datetime.utcnow()

    if now.hour > 10:
        # First war day
        remaining_hours = 10 + (23 - now.hour)
    else:
        # Second war day
        remaining_hours = 10 - now.hour

    return "{} hours".format(remaining_hours)


def is_patch_day():
    return datetime.utcnow().weekday() in PATCH_DAYS


def get_patch_text():
    patch_texts = [
        "@everyone There might be maintenance today, be sure to check with YufineBot for news.",
        "@everyone Today is patch day, check YufineBot's news for details.",
        "@everyone Make sure you use your guild war attacks before maintenance, check the news to make sure you have enough time!",
        "@everyone YufineBot will have news on any maintenance today, Please attack before maintenance starts!"
    ]
    return get_from_list(patch_texts)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, choices=["early", "late"], required=True)
    return parser.parse_args()


def get_message() -> List[str]:
    args = get_parser()
    type_args = args.type
    remaining_time = get_remaining_time()

    messages = []

    if type_args == "early":
        messages.append(get_early_text(remaining_time))
        if is_patch_day():
            messages.append(get_patch_text())
    elif type_args == "late":
        messages.append(get_late_text(remaining_time))

    return messages
