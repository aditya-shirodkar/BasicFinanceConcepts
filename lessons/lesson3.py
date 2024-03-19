# lesson in EBIDTA. Involves no simulations.
import controls


def load_lesson_3():
    print("---")
    print("\x1B[3mEBIDTA\x1B[0m")
    print("---")
    print(
        "EBIDTA stands for \x1B[3mearnings before interest, tax, depreciation, and amortisation\x1B[0m."
    )
    print(
        "To think of it simply, EBIDTA is the revenue earned by a company minus its operating expenses."
    )
    print(
        "Oftentimes, startups (especially tech startups in our age) tend to operate on a large runway of money."
    )
    print(
        "Applying a valuation to these companies is difficult as"
        " they might often make large losses in their early years.\n"
    )
    print("EBIDTA helps with this. EBIDTA can be calculated in two ways:")
    print("* EBIDTA = sales (revenue) - operating expenses, or")
    print(
        "* EBIDTA = net income + taxes + interest expense + depreciation + amortisation\n"
    )

    print(
        "The first method involves a microscopic look at the company,"
        " as calculating operating expenses is an extensive process.\n"
    )
    print("The second method involves a more macroscopic look.")
    print(
        "The reason this calculation works is that net income is usually calculated by"
        " subtracting expenses from your gross income."
    )
    print(
        "Re-adding expenses considered as business expenses"
        " (taxes, interest, depreciation, amortisation) will give the EBIDTA."
    )
    print(
        "These business expenses are all an expected part of new-age startup models,"
        " and so EBIDTA serves as a good metric for their valuation.\n"
    )
    print("What do all these terms mean? Press a key to find out.")
    input()
    print(
        "* The \x1B[3mnet income\x1B[0m is the gross income minus expenses (business or otherwise)."
    )
    print(
        "* \x1B[3mTaxes\x1B[0m are what the business pays to the government and/or"
        " other bodies to continue to operate."
    )
    print(
        "* \x1B[3mInterest expenses\x1B[0m is the money spent on paying interest"
        " on business loans taken by the company."
    )
    print(
        "* \x1B[3mDepreciation\x1B[0m refers to the loss in value of an asset over a specific period of time."
        " An example would be the wear and tear caused to machine parts."
    )
    print(
        "* \x1B[3mAmortisation\x1B[0m is the process of spreading the repayment of loans over a specific timeframe."
        " It usually has to do with long-term assets,"
        " whose costs are spread over the expected lifespans of those assets.\n"
    )
    print(
        "There are different EBIDTA-related terms which can prove useful in evaluating a company."
        " Press a key to explore these."
    )
    input()
    print("* EBIDTA margin = EBIDTA / revenue")
    print(
        "* adjusted EBIDTA adjusts EBIDTA for anomalies particular to the industry = EBIDTA +/- adjustments"
    )
    print("* EBIT = EBIDTA - depreciation - amortisation")
    print(
        "* EBIDTA-to-interest coverage ratio checks if a company is profitable enough to pay its debts ="
        " EBIDTA/total interest payments"
    )
    print(
        "* EBIDTA multiple measures a company's return on investment (ROI) = enterprise value / EBIDTA\n"
    )
    print("That's all for now! Press a key to return to the main menu.")
    input()
    controls.main_menu()
