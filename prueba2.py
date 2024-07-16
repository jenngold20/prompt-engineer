from prueba1 import consulta

context='eres experto en futbol ingles, y quiero que analices la actualidad del: '

prompt=input('Ingrese el equipo de futbol ingles por el cual quisiera consultar: ')

respuesta = consulta(context,prompt)