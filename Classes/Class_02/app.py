1️⃣ Tab (\t)
             
Definition:
\t is used to insert a tab space in a string.

Example:

text = "Name\tAge\tCity"
print(text)

Output:
Name    Age    City
(Each \t creates a tab space)

2️⃣ New Line (\n)
              
Definition:
\n is used to insert a new line in a string.

Example:
text = "Hello\nWorld!"
print(text)

Output:
Hello
World!
(A new line is created after "Hello")

3️⃣ Indexes

Definition:
Indexes allow accessing elements in sequential data types (like strings, lists, and tuples) using their position (starting from 0).

Example:

text = "Python"
print(text[0])  # Output: P
print(text[3])  # Output: h
(Indexing starts from 0, so text[0] is P)

4️⃣ Bytes Datatype

Definition:
The bytes datatype stores binary data (used in files, images, or network communication). It is immutable.

Example:
data = b"Hello"
print(data)         # Output: b'Hello'
print(type(data))   # Output: <class 'bytes'>
print(data[0])      # Output: 72 (ASCII of 'H')
(Adding b before the string creates a bytes object)

5️⃣ split()

Definition:
split() is used to break a string into a list based on a separator.

Example:
text = "apple,banana,grape"
fruits = text.split(",")
print(fruits)  

Output:
['apple', 'banana', 'grape']
(The string is split into a list using "," as a separator)

6️⃣ join()
Definition:
join() is used to combine a list of strings into a single string using a separator.

Example:
fruits = ["apple", "banana", "grape"]
text = " - ".join(fruits)
print(text)

Output:
apple - banana - grape
(All elements are joined using " - " as a separator)

7️⃣ replace()

Definition:
replace() is used to replace a substring with another substring in a string.

Example:
text = "I love Python"
new_text = text.replace("Python", "JavaScript")
print(new_text)

Output:
I love JavaScript
("Python" is replaced with "JavaScript")

8️⃣ Tuple (())

Definition:
A tuple is an ordered, immutable collection of elements.

Ordered → The elements have a defined sequence (indexing is supported).
Immutable → You cannot modify, add, or remove elements after creation.
Uses round brackets (() ).

Example:
my_tuple = (1, 2, 3, "apple", "banana")
print(my_tuple)

Output:
(1, 2, 3, 'apple', 'banana')
Accessing Elements in a Tuple

print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: apple
(Tuples support indexing (0-based) like lists.)

Tuple is Immutable

my_tuple[0] = 10  # ❌ This will give an error
(You cannot modify tuple elements after creation.)

9️⃣ Dictionary ({})

Definition:
A dictionary is an unordered, mutable collection of key-value pairs.

Key-value pairs → Each value has a unique key.
Mutable → You can add, remove, or modify values.
Uses curly brackets ({}).

Example:
my_dict = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore"
}
print(my_dict)

Output:
{'name': 'Ali', 'age': 25, 'city': 'Lahore'}
Accessing Dictionary Values

print(my_dict["name"])  # Output: Ali
print(my_dict["age"])   # Output: 25
(Dictionaries use keys to access values instead of indexes.)

Modifying Dictionary

my_dict["age"] = 26  # Changing age
print(my_dict["age"])  # Output: 26
Adding a New Key-Value Pair
my_dict["country"] = "Pakistan"
print(my_dict)

Output:
{'name': 'Ali', 'age': 26, 'city': 'Lahore', 'country': 'Pakistan'}
Removing a Key-Value Pair

del my_dict["city"]
print(my_dict)

Output:
{'name': 'Ali', 'age': 26, 'country': 'Pakistan'}

🔹 Key Differences Between Tuple and Dictionary
+-------------------+--------------------------------+----------------------------------------+
| Feature          | Tuple ( )                       | Dictionary { }                         |
+-------------------+--------------------------------+----------------------------------------+
| Order            | Ordered ✅                      | Unordered (Python 3.6+ maintains order)|
| Mutability       | Immutable ❌                    | Mutable ✅                             |
| Access           | By index (e.g., tuple[0])       | By key (e.g., dict["name"])           |
| Duplicate Elements| Allowed ✅                      | Keys must be unique ❌                 |
| Use Case         | Fixed data, coordinates,        | Storing related data as                |
|                  | constant values                 | key-value pairs                        |
+-------------------+--------------------------------+----------------------------------------+

🔥 Conclusion
+----------+-----------+------------------------+
| Concept  | Function  | Purpose               |
+----------+-----------+------------------------+
| Tab      | \t        | Adds a tab space      |
| New Line | \n        | Moves text to new line|
| Indexes  | [ ]       | Access elements       |
| Bytes    | b""       | Stores binary data    |
| Split    | split()   | String to list        |
| Join     | join()    | List to string        |
| Replace  | replace() | Replaces in string    |
| Tuple    | ()        | Immutable collection  |
| Dictionary| {}       | Key-value storage     |
+----------+-----------+------------------------+