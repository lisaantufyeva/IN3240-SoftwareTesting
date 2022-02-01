# Cyber-dojo
#Given a list of integers find the closest to zero.
#If there is a tie, choose the positive value.

def main():
    tester()

    list1 = [0.4, 1]
    list2 = [2, 3, 4, 67, 1]
    list3 = [-3, -4, -9, -2]
    list4 = [-3,-4, -5, 3]
    list5 = [-2,2]
    list6 = [0]

    print(closest1(list1))
    print(closest1(list2))
    print(closest1(list3))
    print(closest1(list4))
    print(closest1(list5))
    print(closest1(list6))


def closest1(list):
    if len(list) >= 1:
        closestNumber = list[0]
        for i in list:
            if (i < abs(closestNumber)):
                closestNumber = i
            if (i-abs(closestNumber))==0:
                closestNumber = i
        return closestNumber
    else:
        return "Empty list"


def closest(list):
    if len(list) >= 1:
        closestNumber = list[0]
        for i in list:
            if (i > 0 and i < abs(closestNumber)):
                closestNumber = i
            if (i < 0 and i < abs(closestNumber)):
                closestNumber = i
            if (i > 0 and (i - abs(closestNumber)) == 0):
                closestNumber = i
        return closestNumber
    else:
        return "Empty list"



def tester():
    test_one_element_input()
    test_empty_list()
    test_zero()
    test_positive_numbers()
    test_negative_numbers()
    test_pos_and_neg_numbers()
    test_a_tie()

def test_one_element_input():
    assert closest([1]) == 1
def test_empty_list():
    assert closest([]) == "Empty list"
def test_zero():
    assert closest([0]) == 0
def test_positive_numbers():
    assert closest([2, 3, 4, 67, 1]) == 1
def test_negative_numbers():
    assert closest([-3, -4, -9, -2]) == -2
def test_pos_and_neg_numbers():
    assert closest([-3,-4, -5, 3]) == 3
def test_a_tie():
    assert closest([-2,2]) == 2

main()
