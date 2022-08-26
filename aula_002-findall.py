# metacaracteres . ^ $ * + ? { } [ ] \ | ( )
# | significa OU
# . significa qualquer caractere, exceto quebra de linha
import re 

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|adultos', texto))
print(re.findall(r'João|Maria|ad.tos', texto))
print(re.findall(r'João|Maria|ad...', texto)) # ... qualquer caracter exceto quebra de linha

print(re.findall(r'[Jj]oão|[Mm]aria', texto)) # ['João', 'Maria', 'joão', 'maria', 'Maria']

print(re.findall(r'[a-z]aria', texto))  # qualquer letra entre a e z
print(re.findall(r'[a-zA-Z]aria', texto))  

print(re.findall(r'[0-9]', texto))  # ['1', '0', '1', '9', '7', '0', '5']

print(re.findall(r'jOão|MarIa|ad...', texto, flags=re.IGNORECASE))