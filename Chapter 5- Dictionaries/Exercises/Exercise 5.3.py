# Create a Python glossary
programming_glossary = {
    "Variable": "A named storage location in a program to store data.",
    "Function": "A block of reusable code that performs a specific task.",
    "List": "An ordered collection of items that can be of different data types.",
    "Loop": "A control structure that repeats a set of instructions until a condition is met.",
    "Dictionary": "A collection of key-value pairs for efficient data retrieval."
}

# Add five more Python terms to the glossary
programming_glossary["Module"] = "A file containing Python code, typically used to organize code into reusable units."
programming_glossary["String"] = "A sequence of characters, enclosed in single or double quotes, used for text manipulation."
programming_glossary["Exception"] = "An event that occurs during the execution of a program and disrupts the normal flow of instructions."
programming_glossary["Syntax"] = "The set of rules that dictate how programs are written in a specific programming language."
programming_glossary["Debugging"] = "The process of identifying and fixing errors (bugs) in a program."

# Iterate through the glossary and print each word and its meaning
for word, meaning in programming_glossary.items():
    print(word + ":\n" + meaning + "\n")