# Clean Code with Jaeson – Crafting Professional Software One Chapter at a Time
# Clean Code Chapter 2 – Meaningful Names: How to Name Like a Pro (With Code Examples)

# Use names that reveal intent
# Avoid misleading or vague names
# Be consistent and descriptive
# Add just enough context
# Avoid cute or cryptic naming


d = 3 #Avoid cute or cryptic naming

# Alternative
days_since_last_login = 3 
# Your variable name should make comments unnecessary

account_list = {"acc001": "active"}  # This is a dictionary!

account_status_map = {"acc001": "active"} #Avoid Disinformation

# 3. Make Names Searchable and Pronounceable

def gtmhr():
    pass

def generate_timestamp():
    pass

# If you can’t say it, you won’t explain it. If you can’t search it, you can’t find it.

#  4. Avoid Noise and Redundancy

the_user_data_structure = {...}

user_data = {...}

# Every extra word is a distraction. Strip the noise, keep the meaning.”


# Add Meaningful Context
def calculate():
    pass

def calculate_invoice_total():
    ...


def dpd(d, p):
    return d / p

def calculate_discount_percentage(discount, price):
    return discount / price

# Your function names should read like a sentence. Let the name do the explaining.”
