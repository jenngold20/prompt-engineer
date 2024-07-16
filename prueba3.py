from prueba1 import consulta, archivado

context="Necesito que captures la infortmación que te voy a enviar, pero que captures los datos en formato Json, respetando el siguiente esquema: {'nombre': 'lo que reconozcas como nombre', 'edad': 'entero que reconozcas como edad hasta 100' , 'date': 'la fecha actual pero en formato **/**/****', 'validez':'esto necesito que lo analices tu, si consideras que los datos sin validos entonces que el valor sea true, de manera contraria 'false''}"


nombre = input('ingresa tu nombre  ')
edad =input('ingresa tu edad  ')
date = input('ingresa la fecha de hoy ')
prompt = nombre + edad + date

archivado(context, prompt)