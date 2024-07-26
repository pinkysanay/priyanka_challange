def is_valid_credit_card(card_number):
    # Remove hyphens and check the basic format
    clean_number = card_number.replace('-', '')
    
    # Check if it contains exactly 16 digits
    if len(clean_number) != 16 or not clean_number.isdigit():
        return False
    
    # Check if it starts with 4, 5, or 6
    if clean_number[0] not in '456':
        return False
    
    # Check for valid grouping if hyphens are present
    if '-' in card_number:
        parts = card_number.split('-')
        if len(parts) != 4 or any(len(part) != 4 for part in parts):
            return False
    
    # Check for 4 or more consecutive repeated digits
    for i in range(13):
        if clean_number[i] == clean_number[i+1] == clean_number[i+2] == clean_number[i+3]:
            return False
    
    return True

# Read input
n = int(input().strip())
credit_cards = [input().strip() for _ in range(n)]

# Validate each credit card number and print the result
for card in credit_cards:
    print('Valid' if is_valid_credit_card(card) else 'Invalid')
