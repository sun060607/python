def price(people):
    print("{0} {1}".format(people,people*15000))
def price_morning(people):
    print("{0} {1}".format(people,people*11000))
def price_soldier(people):
    print("{0} {1}".format(people,people*8000))
if __name__ == '__main__':
    price(30)
    price_soldier(50)