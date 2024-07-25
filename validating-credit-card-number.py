import re
def is_valid_credit_card(card_number):

    # Regex pattern to check the validity of the credit card number

    pattern = re.compile(r'^[456]\d{3}(-?\d{4}){3}$')

    # Regex pattern to check for consecutive repeated digits

    consecutive_repeats_pattern = re.compile(r'(\d)\1{3,}')

    # Remove all hyphens from the card number for the consecutive digit check

    card_number_without_hyphens = card_number.replace('-', '')

    # Check if the card number matches the basic pattern and has no consecutive repeated digits

    if pattern.match(card_number) and not consecutive_repeats_pattern.search(card_number_without_hyphens):

        return 'Valid'

    else:

        return 'Invalid'



def validate_credit_cards(n, card_numbers):

    results = []

    for card_number in card_numbers:

        results.append(is_valid_credit_card(card_number))

    return results



# Sample Input

n = 6

card_numbers = [

    "4123456789123456",

    "5123-4567-8912-3456",

    "61234-567-8912-3456",

    "4123356789123456",

    "5133-3367-8912-3456",

    "5123 - 3567 - 8912 - 3456"

]



# Validate the sample input

results = validate_credit_cards(n, card_numbers)

for result in results:

    print(result)