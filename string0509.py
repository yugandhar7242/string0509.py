"""# Major Python String Methods and Built-in Functions

## Content: Major Python String Methods



   Method                                         Description                                                                                                              
   -------------------------------------------    ----------------------------------------------------------------------------------------------------------------------   
     capitalize()                                   Capitalizes the first character of the string, lowercases the rest.                                       
     casefold()                                     Converts string to case-folded version (more aggressive lowercasing, for case-insensitive comparison)    
     center(width, fillchar=' ')                    Returns a new string centered in a field of given width using specified fill character.                 
     count(sub, start=0, end=len)                   Counts occurrences of substring.                                                                        
     encode(encoding='utf-8', errors='strict')      Encodes string to bytes using the specified encoding.                                                   
     endswith(suffix, start=0, end=len)             Returns True if string ends with the specified suffix.   
     expandtabs(tabsize=8)                          Replace tab characters   \t   with spaces; tab size controls how many spaces.                             
     find(sub, start=0, end=len)                    Returns lowest index of substring; returns -1 if not found.                                         
     format(*args, **kwargs)                        Format the string with placeholders.                                                                     
     format_map(mapping)                            Similar to format but uses a mapping (like dict) for substituting.                                       
     index(sub, start=0, end=len)                   Like   find()   but raises   ValueError   if substring not found.                                           
     isalnum()                                      Checks if all characters are alphanumeric and there is at least one character.                          
     isalpha()                                      Checks if all characters are alphabetic and there is at least one character.                             
     isascii()                                      Checks if all characters are ASCII.                                                                      
     isdecimal()                                    Checks if all characters are decimal characters.                                                       
     isdigit()                                      Checks if all characters are digits.                                                                    
     isidentifier()                                 Checks if the string is a valid identifier in Python.  .                                                   
     islower()                                      Checks if all cased characters are lowercase and there's at least one cased character.  .                  
     isnumeric()                                    Checks if all characters are numeric; similar to   isdigit  /  isdecimal   but broader.  .                     
     isprintable()                                  Returns True if all characters in string are printable or the string is empty.  .                          
     isspace()                                      Returns True if string is only whitespace.  .                                                              
     istitle()                                      Returns True if string is title-cased (each word starts with uppercase followed by lowercase).  .          
     isupper()                                      Checks if all cased characters are uppercase.  .                                                           
     join(iterable)                                 Concatenates elements of iterable, inserting this string between them.  .                                  
     ljust(width[, fillchar])                       Left-justify string in a field of given width.  .                                                          
     lower()                                        Converts all characters to lowercase.  .                                                                   
     lstrip([chars])                                Remove leading characters (whitespace by default).  .                                                      
     maketrans()                                    Return a translation table usable for   translate()  .  .                                                    
     partition(sep)                                 Split into a tuple of three: before sep, sep, after sep.  .                                                
     replace(old, new, count=-1)                    Return a copy with all occurrences of old replaced by new (or up to count).  .                             
     rfind(sub, start=0, end=len)                   Like   find   but returns highest index (search from right).  .                                              
     rindex(sub, start=0, end=len)                  Like   index   but from right. Raises if not found.  .                                                       
     rjust(width[, fillchar])                       Right-justify string in a width field.  .                                                                  
     rpartition(sep)                                Similar to partition but splits at the last occurrence.  .                                                 
     rsplit(sep=None, maxsplit=-1)                  Split from right. Returns list of substrings.  .                                                           
     rstrip([chars])                                Remove trailing characters (default whitespace).  .                                                        
     split(sep=None, maxsplit=-1)                   Splits string at sep, returns list.  .                                                                     
     splitlines([keepends=False])                   Splits at line breaks; returns list of lines.  .                                                           
     startswith(prefix[, start, end])               Check if string starts with given substring.  .                                                            
     strip([chars])                                 Trim leading and trailing characters (whitespace by default).  .                                           
     swapcase()                                     Swap case of all characters. Upper→lower, lower→upper.  .                                                  
     title()                                        A titlecased version: each word starts with uppercase, the rest lowercase.  .                              
     translate(table)                               Replace each character using translation table, possibly removing some.  .                                 
     upper()                                        Converts all characters to uppercase.                                                                  
     zfill(width)                                   Pads string with zeros on the left to fill width, preserving sign if present.                           

---

## Additional Built-in Functions Working With Strings

These are not methods on the string object, but built-in Python functions that accept strings (or operate with them) that are very useful. ([DigitalOcean][3])

*   len(s)   — length of string. 
*   ord(c)   — get Unicode code point of character   c  . 
*   chr(i)   — the inverse of   ord  : gives character from code point. 
*   str()   — convert something to string. 
*   ascii()   /   repr()   — get representation of string with escapes etc. 
*   bytes()   /   bytearray()   — convert string (or source) to bytes or bytearray. 

---"""

# 1. `str.isalnum()`

# **Purpose**: Returns `True` if all characters are **alphanumeric** (`a-z`, `A-Z`, `0-9`) and the string is not empty.

### Internal logic (equivalent in Python):

def my_isalnum(s: str) -> bool:
    if len(s) == 0:
        return False
    for ch in s:
        # check if character is letter or digit
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')):
            return False
    return True



print(my_isalnum("abc123"))   # True
print(my_isalnum("abc 123"))  # False (space not allowed)
print(my_isalnum(""))         # False




# 2. `str.find(sub)`
#**Purpose**: Returns the **lowest index** where substring `sub` is found, or `-1` if not found.

### Internal logic (naive version in Python):


def my_find(s: str, sub: str) -> int:
    n, m = len(s), len(sub)
    if m == 0:   # empty substring always found at 0
        return 0
    for i in range(n - m + 1):   # slide window
        if s[i:i+m] == sub:
            return i
    return -1



print(my_find("i am yuzi", "am"))   # 2
print(my_find("hello", "lo"))      # 3
print(my_find("hello", "z"))       # -1
"""

👉 In **CPython**, a more efficient algorithm is used (sometimes **Two-Way string matching** algorithm). But logically it works like above.

---

⚡ Would you like me to also show you the **real C source code from CPython** for `isalnum` and `find`, or keep it only as **Python-equivalent internal logic** for interview purposes?
Good question 👍 You’re asking about **internal code (logic) of string methods** like `isalnum()` and `find()` — i.e., how Python would implement them under the hood.

Python is written in **C (CPython)**, but I’ll explain in **Python-style pseudocode / equivalent code** so you can understand the logic.

---
"""

# 1. `str.isalnum()`

#👉 **Purpose**: Returns `True` if all characters are **alphanumeric** (`a-z`, `A-Z`, `0-9`) and the string is not empty.

### Internal logic (equivalent in Python):


def my_isalnum(s: str) -> bool:
    if len(s) == 0:
        return False
    for ch in s:
        # check if character is letter or digit
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')):
            return False
    return True



print(my_isalnum("abc123"))   # True
print(my_isalnum("abc 123"))  # False (space not allowed)
print(my_isalnum(""))         # False


# 2. `str.find(sub)`

#👉 **Purpose**: Returns the **lowest index** where substring `sub` is found, or `-1` if not found.

### Internal logic (naive version in Python):


def my_find(s: str, sub: str) -> int:
    n, m = len(s), len(sub)
    if m == 0:   # empty substring always found at 0
        return 0
    for i in range(n - m + 1):   # slide window
        if s[i:i+m] == sub:
            return i
    return -1

print(my_find("i am yuzi", "am"))   # 2
print(my_find("hello", "lo"))      # 3
print(my_find("hello", "z"))       # -1