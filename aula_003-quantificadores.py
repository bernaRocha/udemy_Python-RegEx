# metacaracteres . ^ $ * + ? { } [ ] \ | ( )
# * 0 ou n ilimitadas vezes
# + 1 ou n ilimitadas vezes
# ? 0 ou 1
# {n}
# {min, max}
# {10, } 10 ou mais
# {,10} de 0 até 10
# {10} especificamente 10
# {5, 10} De 5 até 10
# ()+ [a-zA-Z0-9]+ 
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



print(re.findall(r'jo+ão', texto, flags=re.I)) # ['João', 'joão', 'Joooooooooão']
print(re.findall(r'jo+ão+', texto, flags=re.I)) # ['João', 'joão', 'Joooooooooãooooooo']
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))  # ['Veeemm']