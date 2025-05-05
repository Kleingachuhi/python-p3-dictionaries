key_vocab = {
    "Mapping": "a data structure in which data is stored in random order \
        and accessed using immutable keys.",
    "Arbitrary": "describes data whose value is unimportant to the data type \
        or structure in which it is contained."
}
print(key_vocab["Arbitrary"])

software_engineer = {
    "languages": ["JavaScript", "Python"],
    "certifications": ["Flatiron School Certificate of Completion"],
    "experience": "3 months and counting!",
}
print(software_engineer["languages"])

def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
    return size_to_ounce_map.get(size)

pour_coffee('tall')

my_dict = {
    "key_one": "value one",
    "key_two": "value two"
}
my_dict["key_one"] = "value has changed"
print(my_dict)

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

for key, value in my_dict.items():
    print(key)
    print(value)