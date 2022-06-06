"""
This module responsible for dealing fee stuff in college
"""


fee_table = {
    'first_year': 300000,
    'second_year': 40000,
    'third_year': 50000,
    'fourth_year': 60000
}


def get_fee(year):
    return fee_table[year]

