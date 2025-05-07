#Comments
# Chapter 4 makes a bold claim: ‘Don’t comment bad code—rewrite it
# the goal should be to write code that doesn’t need them at all.

# 1. Comments Do Not Make Up for Bad Code
# “Express intent in code, not in comments.”
#Bad Code
# Check if user is adult
age = 20
if age > 18:
    ...


if is_adult(age):
    ...

# 2. Explain Yourself in Code
# “Readable code = self-explanatory code.”
# calculate interest
x = p * r * t / 100


interest = calculate_simple_interest(principal, rate, time)


# 3. Good Comments (When Necessary)
# Legal headers

# Clarifications for complex regex

# Warnings of consequences

# TODOs (if tracked properly)

# format matched hh:mm:ss EEE, MMM dd, yyyy
timestamp_pattern = r"\d+:\d+:\d+ \w+, \w+ \d+, \d+"

# 4. Bad Comments (Avoid These)
# ❌ Mumbling: “handles stuff…”

# ❌ Redundant: # increments x

# ❌ Misleading: contradicts the code

# ❌ Noise: javadocs for private methods

# ❌ Commented-Out Code





# 5. Replace with Functions or Variables

if can_edit_document(user, doc):



# Returns list of even numbers from list
def evens(nums):
    return [n for n in nums if n % 2 == 0]


def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

# “Name it right, skip the comment.”









