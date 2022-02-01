'''To try and encourage more sales of the 5 different Harry Potter books they sell, a bookshop has decided to offer discounts of multiple-book purchases.

One copy of any of the five books costs 8 EUR. If, however, you buy two different books, you get a 5% discount on those two books.

If you buy 3 different books, you get a 10% discount.
If you buy 4 different books, you get a 20% discount.
If you go the whole hog, and buy all 5, you get a huge 25% discount.


Your mission is to write a piece of code to calculate the price of any conceivable shopping basket (containing only Harry Potter books), giving as big a discount as possible.

51.20 is the price with the biggest discount.'''

def main():
    
    basket = [1, 2, 3, 4]
    print(calculatePrice(basket))
    tests()
  

def calculatePrice(basket):
    total_price = 0
    
    if (len(basket)>4 and (len(basket)%2) == 0):
        group_max = len(basket)/2
    else: group_max = 5
        
    group_list = create_groups(basket, [], group_max)
    for i in group_list:     
        if len(i) == 1:
            total_price +=i[0].price
        if len(i) == 2:
            groupPrice= i[0].price+i[1].price
            total_price+= (groupPrice) - (groupPrice*0.05)
        if len(i) == 3:
            groupPrice= i[0].price+i[1].price+i[2].price
            total_price+= (groupPrice) - (groupPrice*0.10)
        if len(i) == 4:
            groupPrice= i[0].price+i[1].price+i[2].price+i[3].price
            total_price+= groupPrice - (groupPrice*0.20)
        if len(i) == 5:
            groupPrice= i[0].price+i[1].price+i[2].price+i[3].price+i[4].price
            total_price+= groupPrice - (groupPrice*0.25)
    return total_price

def create_groups(basket,listOfgroups, group_max):
    if len(basket) == 0:
        return listOfgroups
    else:
        group = groupBooks(basket, group_max)
        listOfgroups.append(groupBooks(basket, group_max))
        basket = [i for i in basket if not i in group or group.remove(i)]
        return create_groups(basket,listOfgroups, group_max)

#[1, 2, 3, 4, 1]
def group_books(basket, group_max):
    group = []
    for i in basket:
        if i not in group:
            group.append(i)
            if len(group) == group_max:
                break
    return group

def tests():
    book1 = Book(1, "Harry Potter and the Philosopher's Stone", 8)
    book2 = Book(2, "Harry Potter and the Chamber of Secrets", 8)
    book3 = Book(3, "Harry Potter and the Prisoner of Azkaban", 8)
    book4 = Book(4, "Harry Potter and the Goblet of Fire", 8)
    book5 = Book(5, "Harry Potter and the Order of the Phoenix", 8)

    test_onebook_inbasket(book1)
    test_5percent_discount(book1, book2)
    test_10percent_discount(book1, book2, book3)
    test_20percent_discount(book1, book2, book3, book4)
    test_25percent_discount(book1, book2, book3, book4, book5)
    test_multiple_bookgroups(book1, book2, book3, book4, book5)
    test_empty_basket()

def test_onebook_inbasket():
    assert calculatePrice([book1]) == 8
def test_5percent_discount():
    assert calculatePrice([book1, book2]) == 15.2
    
def test_10percent_discount():
    assert calculatePrice([book1, book2, book3]) == 21.6
    
def test_20percent_discount():
    assert calculatePrice([book1, book2, book3, book4]) == 25.6
    
def test_25percent_discount():
    assert calculatePrice([book1, book2, book3, book4, book5]) == 30

def test_multiple_bookgroups():
    assert calculatePrice([book1, book1, book2, book2, book3, book3, book4, book5])== 51.20

def test_empty_basket():
    assert calculatePrice([]) == 0

class Book:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price



main()
