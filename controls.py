# non-trivial controls for proceeding in the game
import sys
from typing import List, Callable

import lessons.lesson1
import lessons.lesson2
import lessons.lesson3


# each option corresponds to a function call
# incorrect choices will show expanded options, although these are available anyway
def select_option(
    option_descriptions: List[str],
    option_selection: List[Callable[[], None]],
    show_fixed_options: bool = False,
) -> None:
    print("")
    for i in range(len(option_descriptions)):
        print(f"({i+1}) {option_descriptions[i]}")
    if show_fixed_options:
        print("(R) Return to main menu\n(Q) Quit game\n")
    user_input = input()
    if user_input.isdigit():
        if (int(user_input) - 1) in range(len(option_selection)):
            option_selection[int(user_input) - 1]()
        else:
            print("\nUnavailable option. Please choose an option from the following:")
            select_option(
                option_descriptions, option_selection, show_fixed_options=True
            )
    elif user_input.lower() == "q":
        sys.exit()
    elif user_input.lower() == "r":
        main_menu()
    else:
        print("\nUnavailable option. Please choose an option from the following:")
        select_option(option_descriptions, option_selection, show_fixed_options=True)


def main_menu():
    print("Main menu")
    select_option(
        option_descriptions=[
            "Story 1: interest",
            "Story 2: supply and demand",
            "Story 3: EBIDTA",
        ],
        option_selection=[
            lessons.lesson1.load_lesson_1,
            lessons.lesson2.load_lesson_2,
            lessons.lesson3.load_lesson_3,
        ],
        show_fixed_options=True,
    )
