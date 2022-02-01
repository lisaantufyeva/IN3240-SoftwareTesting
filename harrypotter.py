def main():
    
    basket = [1, 2, 3, 4]
    print(calculate_pris(basket))
    tests()
  

def calculate_pris(basket):
    total_price = 0
    if (len(basket) > 4 and (len(basket) % 2) == 0):
        group_max = len(basket)/2
    else: group_max=5
    
    group_list = create_groups(basket,[],group_max)
    print(group_list)
    for i in group_list:    
        if len(i) == 1:
            total_price += 8
        if len(i) == 2:
            total_price+= (8*2) - ((8*2)*0.05)
        if len(i) == 3:
            total_price+= (8*3) - ((8*3)*0.10)
        if len(i) == 4:
            total_price+= (8*4) - ((8*4)*0.20)
        if len(i) == 5:
            total_price+= (8*5) - ((8*5)*0.25)
    return total_price

def create_groups(basket, listofgroups, group_max):  
    if len(basket) == 0:      
        return listofgroups
    else:
            group = group_books(basket, group_max)
            listofgroups.append(group_books(basket, group_max))
            basket = [i for i in basket if not i in group or group.remove(i)]        
            return create_groups(basket, listofgroups, group_max)

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

def test_onebook_inbasket(book1):
    assert calculate_pris([book1]) == 8

def test_5percent_discount(book1, book2):
    assert calculate_pris([book1, book2]) == 15.2
        
def test_10percent_discount(book1, book2, book3):
    assert calculate_pris([book1, book2, book3]) == 21.6
        
def test_20percent_discount(book1, book2, book3, book4):
    assert calculate_pris([book1, book2, book3, book4]) == 25.6
        
def test_25percent_discount(book1, book2, book3, book4, book5):
    assert calculate_pris([book1, book2, book3, book4, book5]) == 30

def test_multiple_bookgroups(book1, book2, book3, book4, book5):
    assert calculate_pris([book1, book1, book2, book2, book3, book3, book4, book5])== 51.20

def test_empty_basket():
    assert calculate_pris([]) == 0

class Book:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    def __str__(self):
        return id



main()
