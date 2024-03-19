# lesson in supply and demand
from _operator import itemgetter
from itertools import product
from random import shuffle
from typing import List, Tuple

import plotext as plt

import controls
import lessons.lesson3


def load_lesson_2():
    print("---")
    print("\x1B[3mSupply and demand\x1B[0m")
    print("---")
    print(
        "The \x1B[3msupply\x1B[0m of a product is the total amount of a specific good"
        " or service that is available to customers."
    )
    print(
        "The \x1B[3mdemand\x1B[0m for a product is the desire for customers to purchase a specific good"
        " or service, and the willingness to pay a particular price for it."
    )
    print(
        "The \x1B[3mlaw of supply and demand\x1B[0m states that as the price of a good"
        " or service rises, its supply increases while its demand decreases, and vice versa.\n"
    )
    print(
        "Let us take a simple example. Imagine if Alice is the only seller of apples in town,"
        " while Bob is the only buyer."
    )
    print(
        "Alice, the seller, generally has a minimum price at which she will sell an apple."
    )
    print("Let's say this price is 10 credits in our example.")
    print(
        "This price usually depends on how much it cost her to make an apple, and how she otherwise values it."
    )
    print("Beneath this price, Alice would much rather just keep the apple.\n")
    print(
        "Similarly, Bob, the buyer, has a maximum price that he is unwilling to exceed when buying an apple."
    )
    print("Let's say this price is 20 credits in our example.")
    print("Bob would gladly pay less than this figure, but refuses to go above it.\n")
    print(
        "If Alice and Bob were to meet, they could come to a deal for an apple, at a price between 10 and 20 credits."
    )
    print("Let's assume they come to a deal at the halfway mark, 15 credits.")
    print(
        "Alice is happy as she gets 5 credits more than her minimum valuation of the apple."
    )
    print(
        "Bob is happy as he managed to buy the apple for 5 credits cheaper than his maximum valuation."
    )
    print(
        "To quantify this, we could say they each gained 5 credits of value."
        " This is known as the \x1B[3msurplus\x1B[0m, a measure of how worthwhile the trade was.\n"
    )
    print(
        "But what if there were other buyers and sellers of apples in town,"
        " each with differing maximum and minimum valuations for apples?"
    )
    print("Let us simulate such an experiment. Press any key to continue.")
    input()
    print("Let us set up some ground rules before we simulate this experiment:")
    print("- Each day, every buyer randomly goes to a seller.")
    print("- Each seller has only one apple to sell.")
    print("- Each buyer buys just one apple a day, to keep the doctor away.")
    print("- Each buyer has a maximum price they're willing to spend on their apple.")
    print(
        "- Each seller has a minimum price they're willing to part with their apple for."
    )
    print("- A buyer and seller will always attempt to meet in the middle.")
    print(
        "- If a transaction doesn't happen, the buyer will try another seller at random."
    )
    print(
        "- The day continues until either all apples are sold or there are no buyers willing to buy any."
    )
    print(
        "- After each day, each buyer and seller adjusts their expectations to reflect their day."
    )
    print(
        "(For sellers, making a transaction will increase the minimum price by 10%, and"
        " not making a transaction will decrease the minimum price by 10%."
        " It's the opposite for buyers and their maximum price.)\n"
    )
    print("Choose an option from the list below.")
    lesson_2_options()


def lesson_2_options():
    controls.select_option(
        option_descriptions=[
            "1 buyer, 1 seller",
            "1 buyer, 2 sellers",
            "2 buyers, 1 seller",
            "2 buyers, 2 sellers",
            "Proceed to lesson 3",
        ],
        option_selection=[
            load_lesson_2_1,
            load_lesson_2_2,
            load_lesson_2_3,
            load_lesson_2_4,
            lessons.lesson3.load_lesson_3,
        ],
    )


def load_lesson_2_1():
    print("\x1B[3m1 buyer, 2 sellers\x1B[0m")
    print("Here, Alice is a seller while Bob is a buyer. On day 0:")
    print("- Alice's minimum sale price is 10 credits.")
    print("- Bob's maximum purchase price is 20 credits.")
    print("Press any key to continue.")
    input()
    market_simulator(
        buyers=[("Bob", 20)],
        sellers=[("Alice", 10)],
    )
    print(
        "As you can see, given that there's no other buyer or seller, neither Alice nor Bob has an advantage."
    )
    print(
        "Therefore, the minimum/maximum acceptable prices converge to an equilibrium point.\n"
    )
    print("Continue with your lessons:")
    lesson_2_options()


def load_lesson_2_2():
    print("\x1B[3m1 buyer, 2 sellers\x1B[0m")
    print("Here, Alice and Charlie are sellers while Bob is a buyer. On day 0:")
    print("- Alice's minimum sale price is 10 credits.")
    print("- Charlie's minimum sale price is 12 credits.")
    print("- Bob's maximum purchase price is 20 credits.")
    print("Press any key to continue.")
    input()
    market_simulator(
        buyers=[("Bob", 20)],
        sellers=[("Alice", 10), ("Charlie", 12)],
    )
    print("As you can see, the lone buyer has an advantage.")
    print(
        "Bob can drive the price down and the sellers would have to lower"
        " their minimum expectation to compete with each other."
    )
    print(
        "This scenario would persist until one of them drops out (i.e., the supply reduces).\n"
    )
    print(
        "You can also observe how the value gained as surplus primarily goes to the buyer."
    )
    print("Continue with your lessons:")
    lesson_2_options()


def load_lesson_2_3():
    print("\x1B[3m2 buyers, 1 seller\x1B[0m")
    print("Here, Alice is a seller while Bob and Dylan are buyers. On day 0:")
    print("- Alice's minimum sale price is 10 credits.")
    print("- Bob's maximum purchase price is 20 credits.")
    print("- Dylan's maximum purchase price is 18 credits.")
    print("Press any key to continue.")
    input()
    market_simulator(
        buyers=[("Bob", 20), ("Dylan", 18)],
        sellers=[("Alice", 10)],
    )
    print("As you can see, the lone seller has an advantage.")
    print(
        "Alice can drive the price up and the buyers would have to lower"
        " their maximum purchase price to compete with each other."
    )
    print(
        "This scenario would persist until one of them drops out (i.e., the demand reduces).\n"
    )
    print(
        "You can also observe how the value gained as surplus primarily goes to the seller."
    )
    print("Continue with your lessons:")
    lesson_2_options()


def load_lesson_2_4():
    print("\x1B[3m2 buyers, 2 sellers\x1B[0m")
    print(
        "Here, Alice and Charlie are sellers while Bob and Dylan are buyers. On day 0:"
    )
    print("- Alice's minimum sale price is 10 credits.")
    print("- Charlie's minimum sale price is 12 credits.")
    print("- Bob's maximum purchase price is 20 credits.")
    print("- Dylan's maximum purchase price is 18 credits.")
    print("Press any key to continue.")
    input()
    market_simulator(
        buyers=[("Bob", 20), ("Dylan", 18)],
        sellers=[("Alice", 10), ("Charlie", 12)],
    )
    print(
        "As you can see, neither buyers nor sellers have an advantage,"
        " given that the supply and demand are both 2 apples a day."
    )
    print(
        "Therefore, the minimum/maximum acceptable prices converge to an equilibrium point.\n"
    )
    print("Continue with your lessons:")
    lesson_2_options()


# trivial simulator for a market where each seller sells one item and each buyer buys one item
# can be made more dynamic by using classes
# sequentially plots the maximum purchase price for buyers alongside the minimum sale price for sellers
def market_simulator(buyers: List[Tuple[str, int]], sellers: List[Tuple[str, int]]):
    fast_forward = False
    for i in range(11):
        shuffle(buyers)
        shuffle(sellers)
        buyer_seller_map = list(product(buyers, sellers))
        buyer_deals = [
            (
                buyer_seller[0][0],
                buyer_seller[1][0],
                (buyer_seller[0][1] + buyer_seller[1][1]) / 2,
            )
            for buyer_seller in buyer_seller_map
            if (buyer_seller[0][1] >= buyer_seller[1][1])
        ]
        buyer_deals = [(b, s, p) for (b, s, p) in buyer_deals if p > 0]
        buyer_best_deals = []
        for j in range(len(buyers)):
            try:
                buyer_best_deal = min(buyer_deals, key=itemgetter(2))
            except:
                continue
            buyer_deals = [
                (b, s, p)
                for (b, s, p) in buyer_deals
                if s != buyer_best_deal[1] and b != buyer_best_deal[0]
            ]
            buyer_best_deals.append(buyer_best_deal)
        buyers_making_deals = [b for (b, _, _) in buyer_best_deals]
        sellers_making_deals = [s for (_, s, _) in buyer_best_deals]
        buyers = [
            (b, p * 0.9) if b in buyers_making_deals else (b, p * 1.1)
            for (b, p) in buyers
        ]
        sellers = [
            (s, p * 1.1) if s in sellers_making_deals else (s, p * 0.9)
            for (s, p) in sellers
        ]
        if fast_forward:
            if i != 10:
                continue

        plt.subplots(1, 2)
        plt.subplot(1, 1).title("Buyers")
        plt.bar([buyer[0] for buyer in buyers], [buyer[1] for buyer in buyers])
        plt.xlabel("Time")
        plt.ylabel("Maximum purchase price")

        plt.subplot(1, 2).title("Sellers")
        plt.bar([seller[0] for seller in sellers], [seller[1] for seller in sellers])
        plt.xlabel("Time")
        plt.ylabel("Minimum sale price")
        plt.show()
        if i != 10:
            print(
                "Press F to fast-forward to the end, or any other key to proceed 1 year."
            )
            user_input = input()
            if user_input.lower() == "f":
                fast_forward = True
