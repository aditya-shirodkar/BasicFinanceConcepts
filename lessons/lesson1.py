# lesson in simple and compound interest
import plotext as plt

import controls
import lessons.lesson2


def load_lesson_1():
    print("---")
    print("\x1B[3mInterest\x1B[0m")
    print("---")
    print(
        "When someone lends you money (also known as the \x1B[3mprincipal\x1B[0m),"
        " they usually expect to get back more than the amount they'd lent,"
    )
    print(
        "This is because, otherwise, they might have used the money elsewhere to make a \x1B[3mprofit\x1B[0m,"
        " i.e., earn more money than they'd spent."
    )
    print(
        "The additional sum that you must pay back is known as the \x1B[3minterest\x1B[0m due.\n"
    )
    print(
        "Alice wants to loan some money from a bank so she can setup an apple orchard. There are two banks in town."
    )
    print(
        "Bank 1 and Bank 2 both offer interest rates of 10% annually on the principal."
    )
    print(
        "However, Bank 1 offers a simple interest rate on its loan, whereas Bank 2 offers a compound interest rate.\n"
    )
    print("Which bank's loan should she go for?")
    controls.select_option(
        option_descriptions=["Bank 1", "Bank 2", "I don't know"],
        option_selection=[load_lesson_1_1, load_lesson_1_1, load_lesson_1_1],
    )


# any choice leads to this function
# sequentially plots the simple and compound interest at the same rate for the same principal
def load_lesson_1_1():
    print(
        "The correct answer is that Alice should take her loan from Bank 1, which offers simple interest.\n"
    )
    print(
        "Simple interest is calculated only on the principal that was initially borrowed."
    )
    print(
        "Compound interest is calculated such that, every year, you must pay interest not only on the principal,"
        " but also on the \x1B[3minterest accumulated so far\x1B[0m."
    )
    print(
        "You may have noticed that we never mentioned the time period of the loan or the actual amount borrowed."
    )
    print(
        "This is because, at the same rate %, simple interest always accumulates slower than (or at the same pace as)"
        " compound interest.\n"
    )
    print(
        "Let us assume Alice first borrowed 100000 credits from the bank (the principal), and observe how the interest"
        " owed at 10% annually grows in time each year."
    )
    simple_interest = [int(100000 * i * 0.1) for i in range(11)]
    compound_interest = [int(100000 * 1.1**i - 100000) for i in range(11)]
    xticks = [i for i in range(11)]

    fast_forward = False
    for i in range(11):
        if fast_forward:
            if i != 10:
                continue
        plt.subplots(1, 2)
        plt.subplot(1, 1).title("Simple interest")
        plt.scatter(xticks, simple_interest[: i + 1], marker="x")
        plt.xticks(xticks)
        plt.ylim(0, 160000)
        plt.yfrequency(9)
        plt.xlabel("Time")
        plt.ylabel("Interest owed")

        plt.subplot(1, 2).title("Compound interest")
        plt.scatter(xticks, compound_interest[: i + 1], marker="o")
        plt.xticks(xticks)
        plt.ylim(0, 160000)
        plt.yfrequency(9)
        plt.xlabel("Time")
        plt.ylabel("Interest owed")
        plt.show()
        if i != 10:
            print(
                "Press F to fast-forward to the end, or any other key to proceed 1 year."
            )
            user_input = input()
            if user_input.lower() == "f":
                fast_forward = True

    print(
        "As you can see, at the same rate of interest, compound interest grows faster year-over-year.\n"
    )
    print("Choose one of the following options:")
    controls.select_option(
        option_descriptions=[
            "Try problems in interest",
            "Relearn this lesson",
            "Proceed to lesson 2",
        ],
        option_selection=[load_lesson_1, load_lesson_1, lessons.lesson2.load_lesson_2],
    )
