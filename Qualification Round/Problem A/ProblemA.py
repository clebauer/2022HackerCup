### Links:
### * Hackercup Link: https://www.facebook.com/codingcompetitions/hacker-cup
### * Problem A Link: https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/A

###--------- Imports ----------###
import pandas as pd
from collections import Counter

###--------- Data Input and Sanitization ----------###
input_df = pd.read_csv("second_hands_input.txt", header=None, names=["values"])
input_df['values'] = input_df['values'].apply(lambda row: [int(x) for x in row.split()])

# Grab number of examples
num_input = input_df['values'][0][0]
input_df = input_df[1:].reset_index(drop=True)

def run_tests(num_parts, max_per_case, num_styles):
    # Test 1: Are any s values greater than 2?
    if max(Counter(num_styles).values()) > 2:
        return "NO"
    # Test 2: Is the total number divided in half still bigger than the max?
    if num_parts / 2 > max_per_case:
        return "NO"

    # Then,
    return "YES"

with open("Problem A - ANSWERS.txt", "a") as myfile:
    for x in range(0,len(input_df),2):
        num_parts, max_per_case = input_df['values'][x]
        num_styles = input_df['values'][x+1]

        status = run_tests(num_parts, max_per_case, num_styles)
        myfile.write(f"Case #{x//2 + 1}: {status}\n")
