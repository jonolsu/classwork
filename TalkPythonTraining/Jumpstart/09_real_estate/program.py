import csv
import os
from data_types import Purchase

try:
    import statistics  # only in Python 3.4.3+
except:
    import statistics_standin_for_py2 as statistics


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-------------------------------------')
    print('       Real Estate Data Mining App')
    print('-------------------------------------')
    print()


def query_data(data):
    data.sort(key=lambda p: p.price)
    high_purchase = data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))
    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    prices = [
        p.price  # projection or items
        for p in data  # the set to process
        ]

    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(ave_price)))

    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        if announce(p, '2-bedrooms, found{}'.format(p.beds)) and p.beds == 2 # test / condition
    )
    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqft = statistics.mean((p.sq__ft for p in homes))
    print("The average price of a 2-bedroom home is ${:,}, baths = {}, sq ft = {:,}"
          .format(round(ave_price,2), round(ave_baths,1), round(ave_sqft,1)))


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        print(purchases[8].__dict__)
    return purchases


def announce(item, msg):
    print("Pulling item {} for {}".format(item,msg))
    return item

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv'))


if __name__ == '__main__':
    main()
