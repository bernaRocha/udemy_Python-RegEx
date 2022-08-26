import re

texto = """
<p>Frase 1<p/> <p>Frase 2<p/> <p>Frase 3<p/> <div>Frase 4<div/>

"""

# print(re.findall(r'<[pdiv]{1,3}>', texto)) # ['<p>', '<p>', '<p>', '<div>']
# print(re.findall(r'<[pdiv]{1,3}>', texto)) 

texto = '''
<p>Frase 1<p/> <p>Eita<p/> <p>Qualquer coisa<p/> <div><div/>
'''

# print(re.findall(r'<[pdiv]{1,3}>.*', texto2)) # ['<p>Frase 1<p/> <p>Eita<p/> <p>Qualquer coisa<p/> <div><div/>']
print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))