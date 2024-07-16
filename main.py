import openai #llamado a la libreria

#Define tu clave de API de OpenAI
api_key = ""

#Configura la clave de API
openai.api_key = api_key #llamado a la api_key

#Funcion para generar una tarea pendiente para una reunion especifica
def generar_tarea_para_reunion(reunion):
    #Define el prompt que solicita la tarea pendiente
    prompt = f"Genera una tarea pendiente para la siguiente reunión: {reunion}\nTarea:"
    
    #Llama  ala API de OpenAI para generar el texto basado en el prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
       
    )#Devuelve la respuesta de la API de OpenAI
    tarea = response.choices[0].text.strip()
    return tarea

#Ejemplo de uso
if __name__ == "__main__":
    reunion = "Reunión de equipo para el próximo meetup"
    #Genera una tarea pendiente llamando a la función
    tarea = generar_tarea_para_reunion(reunion)
    
    #Imprime la tarea pendiente generada junto con el nombre de la reunión
    print(f"Tarea pendiente para '{reunion}':\n{tarea}")
    
   