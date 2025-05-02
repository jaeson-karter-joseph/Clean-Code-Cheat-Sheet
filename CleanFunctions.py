# # # CHAPTER 3: FUNCTIONS

# # Key Concepts Covered:

# Functions should be small – really small
def process_user(user_data): #Bad Function
    # fetch, validate, update DB, send email – all in one

def process_user(user_data): #Good Function
    validated = validate_user(user_data)
    save_to_db(validated)
    send_welcome_email(validated)
# Each function should do only one clear, isolated task



# Do one thing, and one thing only

def generate_report(data):
    cleaned = clean_data(data)
    analyzed = analyze_data(cleaned)
    # save_to_db(analyzed) # Bad: Side effect
    return format_report(analyzed)

# Use descriptive names
def handle(data): # Bad: What does this do?
    ...

def sanitize_and_store_user_input(data): # Good: Clear and descriptive
    ...
# If your function name is vague, your function probably is too.”


# One level of abstraction per function
def generate_report(data):
    cleaned = []
    for item in data:
        if item.strip() != "":
            cleaned.append(item.strip())

    analyzed = {}
    for item in cleaned:
        if item in analyzed:
            analyzed[item] += 1
        else:
            analyzed[item] = 1

    report = f"Report Generated:\n{analyzed}"
    return report
# Problem: This function mixes data cleaning, analysis, and report formatting — all different levels of abstraction.

def generate_report(data):
    cleaned = clean_data(data)
    analysis = analyze_data(cleaned)
    return format_report(analysis)


def clean_data(data):
    return [item.strip() for item in data if item.strip() != ""]


def analyze_data(cleaned_data):
    result = {}
    for item in cleaned_data:
        result[item] = result.get(item, 0) + 1
    return result


def format_report(analysis):
    return f"Report Generated:\n{analysis}"
# Why it's better:

# generate_report() operates at a high level, abstracting away details.

# Lower-level details are encapsulated in their own clearly named functions.

# Easier to test, maintain, and read.



# Prefer fewer arguments

def create_user(name, age, email, address, role):
    ...
def create_user(user_info):
    ...


# No side effects
def get_config():
    set_user_env()  # side effect!
    return config

def get_config():
    return config




# Use exceptions, not error codes

def divide(a, b):
    if b == 0:
        return -1
    return a / b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
