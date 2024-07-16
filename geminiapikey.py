import pathlib
import textwrap

#pip install IPython
#pip install google-generativeai

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown



def to_markdown(text):
  text= text.replace('•', ' *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY= 'AIzaSyC2kzAGBY1e74SKdz4yE9jLl-qsV3DC0w0'


genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model= genai.GenerativeModel('gemini-1.0-pro')

context = 'Quiero que seas un experto en cocina argentina. Necesito que me sugieras recetas no muy caras y de fácil preparación. En breve te voy a pedir que me enseñes a preparar, devolvela en formato Json :  '

prompt = input('Dime en una sola oración qué comida queres aprender a cocinar: ')


def consulta(context, prompt):
    response = model.generate_content(context + prompt)
    archivo = response.text
    with open('archivo.txt', 'w') as f:
        f.write(archivo)

    return display(response.text)
  
  
  
import json
def consulta(context, prompt):
    response = model.generate_content(context + prompt)
    archivo = response.text
    with open('archivo.json', 'w') as f:
       json.dump(response.text, f)

    return display(response.text)
 
 
consulta(context, prompt)
  
# Commented out IPython magic to ensure Python compatibility.
# %%time
# response = model.generate_content("dar la bienvenida al curso de IA")

#response.text

#to_markdown(response.text)

#response.candidates

#connect to the API and send an example message

#text = 'What is the velocity of an unladen swallow?' #@param {type: 'string'}

#model = genai.GenerativeModel('gemini-pro')
#chat = model.start_chat(history=[])

#response = chat.send_message(text)
#response.text