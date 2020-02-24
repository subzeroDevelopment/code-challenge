"""
Have the function Splitter(string) read the string, find the separator return it and the number of strings.

For example:
abc,def,ghi   -> should return ',',3
12ab-cde-123-hij  -> should return '-',4
abcdefghi1234 -> should return None,0
""(empty string) -> should return None,0

The strings only can contain letters(a-z or A-Z) and numbers(0-9).
The separators are special characters as: ",",".","-","_","*","?","#","&","|","+","~" etc.
"""

def Splitter(string:str):
    return "",0