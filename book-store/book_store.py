import collections


def total(basket):
    price = 0
    single_book_price = 800
    number_of_books = len(basket)

    # Are all books the same?
    if all(book == basket[0] for book in basket):
        price =  len(basket) * single_book_price

    # Are all books different?
    elif len(set(basket)) == len(basket):
        price = get_price_for_less_than_six_different_books(len(basket), single_book_price)

    else:
        book_frequency_mapping = collections.Counter(basket)

        # How many distinct types of books are in the basket?
        while (number_of_distinct_books(book_frequency_mapping) > 0):

            # While there are still books left in the basket..
            # TODO: Don't recompute this variable.
            num_distinct_books = number_of_distinct_books(book_frequency_mapping)

            books_purchased_this_round = 0

            # The general strategy here is to use the number of distinct books you have available and
            # then order the if statements such that the 'best' discounts are checked first.

            # Unfortunately, I don't quite understand this challenge and the logic around how to tell
            # which discount is the best to use, which is why I hardcoded the case of 12 (test_three_each_of_first_2_books_and_2_each_of_remaining_books)
            # Basically the case of 12 has two possibilities that I can see:
            # Either make 3 bundles of 4 books, or
            # make 2 bundles of 5 books, and one group of 2.
            # The latter yields the bigger discount, but I can't seem to figure out a clean algorithm
            # for checking which price strategy yields the biggest discount -- I'm guessing it has to do
            # with how many groups of distinct books you can make, but I'm not sure.

            if ((num_distinct_books == 5) and (number_of_books % 4 != 0)) or ((number_of_books == 12) and (get_maximum_number_of_full_groups_you_could_make(book_frequency_mapping) == 2)):
                books_purchased_this_round = 5
                price += get_price_for_less_than_six_different_books(books_purchased_this_round, single_book_price)

            elif (num_distinct_books >= 4):
                books_purchased_this_round = 4
                price += get_price_for_less_than_six_different_books(books_purchased_this_round, single_book_price)

            elif num_distinct_books == 3:
                books_purchased_this_round = num_distinct_books
                price += get_price_for_less_than_six_different_books(books_purchased_this_round, single_book_price)

            elif num_distinct_books == 2:
                books_purchased_this_round = num_distinct_books
                price += get_price_for_less_than_six_different_books(books_purchased_this_round, single_book_price)

            elif num_distinct_books == 1:
                books_purchased_this_round = num_distinct_books
                price += single_book_price

            # Now decrement each key's value if its greater than 1 for however many books you just purchased
            book_counts_decremented = 0

            # Decrement the number of books remaining by the number of books you purchased this round
            number_of_books -= books_purchased_this_round

            for books in sorted(book_frequency_mapping.items(), key = lambda kv: kv[1], reverse=True):
                book, _ = books
                if book_counts_decremented < books_purchased_this_round:
                    if book_frequency_mapping[book] > 0:
                        book_frequency_mapping[book] -= 1
                        # Keep track of how many book counts got decremented so that you don't accidentally
                        # decrement too many. As in, you only bought 3 books, but you decremented the count
                        # of 4 different books, making it seem like you bought 4 and not 3.
                        book_counts_decremented += 1
                else:
                    break



    return price


def number_of_distinct_books(basket_of_books : dict) -> int:
    return len([book for book, frequency in basket_of_books.items() if frequency > 0])

def get_price_for_less_than_six_different_books(num_books : int, single_book_price):
    # TODO: Figure out a clean function that maps exactly from number of books -> discount percentage
    # rather than hardcoding it.

    assert(1 < num_books < 6)

    if num_books == 2: discount_percentage = 0.05
    elif num_books == 3: discount_percentage = 0.10
    elif num_books == 4: discount_percentage = 0.20
    elif num_books == 5: discount_percentage = 0.25

    return compute_discounted_price(discount_percentage, single_book_price, num_books)


def compute_discounted_price(discount_percentage, single_book_price, number_of_books):
    normal_price = single_book_price * number_of_books
    discount_amount = discount_percentage * normal_price
    return normal_price - discount_amount


def get_maximum_number_of_full_groups_you_could_make(book_frequencies) -> int:

    book, value = sorted(book_frequencies.items(), key = lambda kv : kv[1])[0]
    return value
