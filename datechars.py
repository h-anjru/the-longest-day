from datetime import datetime
import pandas as pd


def int_to_alpha(num):
    """
    Change an integer to an alphabetical number.
    https://stackoverflow.com/a/32640407
    """

    d = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

    k = 1000
    m = k * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred ' + int_to_alpha(num % 100)

    if (num < m):
        if num % k == 0: return int_to_alpha(num // k) + ' thousand'
        else: return int_to_alpha(num // k) + ' thousand ' + int_to_alpha(num % k)


# integers to ordinals for dates of month...might as well be a dict
nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
    13: "thirteenth",
    14: "fourteenth",
    15: "fifteenth",
    16: "sixteenth",
    17: "seventeenth",
    18: "eighteenth",
    19: "nineteenth",
    20: "twentieth",
    21: "twenty-first",
    22: "twenty-second",
    23: "twenty-third",
    24: "twenty-fourth",
    25: "twenty-fifth",
    26: "twenty-sixth",
    27: "twenty-seventh",
    28: "twenty-eighth",
    29: "twenty-ninth",
    30: "thirtieth",
    31: "thirty-first",
}

# 00:00:00 02 Jan 0001; datetime won't go to 01 Jan 0001?
begin = -62135492638

# 23:59:59 31 Dec 9999
end = 253402318799

# initialize lists to store results
all_days = []
all_dates = []
all_months = []
all_years = []
date_strings = []
string_lengths = []

# iterate over every day
now = begin + 43200  # keep it around noon to avoid that leap second mess

while now < end:
    date_obj = datetime.fromtimestamp(now)

    # break it up to easily pass some elements to other functions
    day = date_obj.strftime("%A")
    all_days.append(day)

    date_int = int(date_obj.strftime("%d"))
    date = nth[date_int]
    all_dates.append(date_int)

    month = date_obj.strftime("%B")
    all_months.append(month)

    year_int = int(date_obj.strftime("%Y"))
    year = int_to_alpha(year_int)
    all_years.append(year_int)

    string = f"{day}, the {date} of {month}, year {year}"
    date_strings.append(string)

    string_lengths.append(len(string))

    now += 86400  # some leap seconds along the way, but not 86400 of them!

# put lists into dataframe
date_a_frame = pd.DataFrame(
    {
        "Day": all_days,
        "Date": all_dates,
        "Month": all_months,
        "Year": all_years,
        "String": date_strings,
        "Length": string_lengths,
    }
)

# shift index to become day since beginning (Jan 2)
date_a_frame.index += 2
date_a_frame.index.name = 'Day of CE'

# sort and save
sorted = date_a_frame.sort_values(by=["Length"], ascending=[False])
sorted.to_csv("datelength.csv", sep=",", encoding="utf-8")
