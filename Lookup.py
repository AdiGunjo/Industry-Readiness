# Lookup tables 
# Commit message change commit nothing special characters

ones_eng = {
    0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
    14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
    17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}

tens_eng = {
    2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
    6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
}

ones_hin = {
    0: "", 1: "एक", 2: "दो", 3: "तीन", 4: "चार", 5: "पाँच",
    6: "छह", 7: "सात", 8: "आठ", 9: "नौ", 10: "दस",
    11: "ग्यारह", 12: "बारह", 13: "तेरह", 14: "चौदह",
    15: "पंद्रह", 16: "सोलह", 17: "सत्रह", 18: "अठारह",
    19: "उन्नीस"
}

tens_hin = {
    2: "बीस", 3: "तीस", 4: "चालीस", 5: "पचास",
    6: "साठ", 7: "सत्तर", 8: "अस्सी", 9: "नब्बे"
}

ones_mar = {
    0: "", 1: "एक", 2: "दोन", 3: "तीन", 4: "चार", 5: "पाच",
    6: "सहा", 7: "सात", 8: "आठ", 9: "नऊ", 10: "दहा",
    11: "अकरा", 12: "बारा", 13: "तेरा", 14: "चौदा",
    15: "पंधरा", 16: "सोळा", 17: "सतरा", 18: "अठरा",
    19: "एकोणीस"
}

tens_mar = {
    2: "वीस", 3: "तीस", 4: "चाळीस", 5: "पन्नास",
    6: "साठ", 7: "सत्तर", 8: "ऐंशी", 9: "नव्वद"
}


def two_digit(n, ones, tens):
    if n < 20:
        return ones[n]

    return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")


def three_digit(n, ones, tens, hundred):
    if n < 100:
        return two_digit(n, ones, tens)

    result = ones[n // 100] + " " + hundred

    if n % 100 != 0:
        result += " " + two_digit(n % 100, ones, tens)

    return result


# English
def english(n):
    if n == 0:
        return "Zero"

    result = ""

    crore = n // 10000000
    n %= 10000000

    lakh = n // 100000
    n %= 100000

    thousand = n // 1000
    n %= 1000

    if crore:
        result += three_digit(crore, ones_eng, tens_eng, "Hundred") + " Crore "

    if lakh:
        result += two_digit(lakh, ones_eng, tens_eng) + " Lakh "

    if thousand:
        result += two_digit(thousand, ones_eng, tens_eng) + " Thousand "

    if n:
        result += three_digit(n, ones_eng, tens_eng, "Hundred")

    return result.strip()


# Hindi
def hindi(n):
    if n == 0:
        return "शून्य"

    result = ""

    crore = n // 10000000
    n %= 10000000

    lakh = n // 100000
    n %= 100000

    thousand = n // 1000
    n %= 1000

    if crore:
        result += two_digit(crore, ones_hin, tens_hin) + " करोड़ "

    if lakh:
        result += two_digit(lakh, ones_hin, tens_hin) + " लाख "

    if thousand:
        result += two_digit(thousand, ones_hin, tens_hin) + " हजार "

    if n:
        result += three_digit(n, ones_hin, tens_hin, "सौ")

    return result.strip()


# Marathi
def marathi(n):
    if n == 0:
        return "शून्य"

    result = ""

    crore = n // 10000000
    n %= 10000000

    lakh = n // 100000
    n %= 100000

    thousand = n // 1000
    n %= 1000

    if crore:
        result += two_digit(crore, ones_mar, tens_mar) + " कोटी "

    if lakh:
        result += two_digit(lakh, ones_mar, tens_mar) + " लाख "

    if thousand:
        result += two_digit(thousand, ones_mar, tens_mar) + " हजार "

    if n:
        result += three_digit(n, ones_mar, tens_mar, "शे")

    return result.strip()


num = int(input("Enter number (0 to 99999999): "))

if 0 <= num <= 99999999:
    print("English :", english(num))
    print("Hindi   :", hindi(num))
    print("Marathi :", marathi(num))
else:
    print("Number out of range")