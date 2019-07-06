def recite(start_verse, end_verse):
    verses = []

    for current_verse_number in range(start_verse, end_verse + 1):
        current_verse : str = ""
        day_as_ordinal: str = get_ordinalized_name_of_number(current_verse_number)
        starting_string: str = f"On the {day_as_ordinal} day of Christmas my true love gave to me: "
        current_verse += starting_string
        items_printed_on_current_verse = 0

        for day_number in range(current_verse_number, 0, -1):
            if items_printed_on_current_verse != 0 and day_number == 1:
                current_verse += "and "

            current_verse += retrieve_item_for_verse_number(day_number)
            items_printed_on_current_verse += 1

            if (day_number == 1):
                current_verse += "."

            else:
                current_verse += ", "

        verses.append(current_verse)

    return verses


def retrieve_item_for_verse_number(verse : int) -> str:
    items_for_each_day = {
        1 : "a Partridge in a Pear Tree",
        2 : "two Turtle Doves",
        3 : "three French Hens",
        4 : "four Calling Birds",
        5 : "five Gold Rings",
        6 : "six Geese-a-Laying",
        7 : "seven Swans-a-Swimming",
        8 : "eight Maids-a-Milking",
        9 : "nine Ladies Dancing",
        10 : "ten Lords-a-Leaping",
        11 : "eleven Pipers Piping",
        12 : "twelve Drummers Drumming"
    }

    return items_for_each_day.get(verse)

def get_ordinalized_name_of_number(number: int) -> str:
    ordinals = {
        1 : "first",
        2 : "second",
        3 : "third",
        4 : "fourth",
        5 : "fifth",
        6 : "sixth",
        7 : "seventh",
        8 : "eighth",
        9 : "ninth",
        10 : "tenth",
        11 : "eleventh",
        12 : "twelfth"
    }

    return ordinals.get(number)

