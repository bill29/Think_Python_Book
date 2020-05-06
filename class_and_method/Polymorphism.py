def histogram(s):
    """

    :param s:object
    :return: dict , key: word, value: histogram of word in s
    """
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
a_list = ['dan', 'dan', 'minh', 'hanh']
a_dict = {'dan':1, 'dan':2, 'minh':2, 'hanh':1}
a_tuple = ('dan', 'dan', 'minh', 'hanh')

#print result for polymorphism for dict, list, tuple
def print_result():
    print(histogram(a_list))
    print(histogram(a_dict)) #dict dont add a same key ....
    print(histogram(a_tuple))
print_result()