from logic import calculate_discount
from window import setupUI
from repository import get_partners

def main():

    partner_data = get_partners()

    for partner in partner_data:
        calculate_discount(partner)

    setupUI(partner_data)

if __name__ == '__main__':
    main()