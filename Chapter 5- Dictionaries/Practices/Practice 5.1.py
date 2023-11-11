my_information = {
    "Name": "Asmina Shehzadha",
    "Age": "19",
    "Mother's Name": "Shobitha Akbar",
    "Father's Name": "Akbar Hydrose",
    "Hobbies": ["Dancing", "Watching", "Reading", "Listening to Music" ],
    "University": "Bathspa University",
    "Course": "Cyber Security",
    "contact_information": {
        "email": "asminashehzadha@gmail.com",
        "Instagram": "minss_sheh",
    }
}

# Accessing information
print("Name:", my_information["Name"])
print("Age:", my_information["Age"])
print("University:", my_information["University"])
print("Hobbies:", ", ".join(my_information["Hobbies"]))
