# https://docs.python.org/pt-br/3/library/re.html

import re

# findall search sub > 
# compile

string = 'Isto é um teste de expressões regulares.'
print(re.search(r'teste', string)) # <re.Match object; span=(10, 15), match='teste'>
print(re.findall(r'teste', string)) # ['teste']
print(re.sub(r'teste', 'ABCD', string)) # Isto é um ABCD de expressões regulares.


regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))