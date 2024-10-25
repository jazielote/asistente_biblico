import flet as ft
import google.generativeai as genai

modelo = genai.GenerativeModel('gemini-pro')

GOOGLE_API_KEY = "AIzaSyBXte6GGGa7MJMbG8WRPIBLB69D1R3IX0o"

genai.configure(api_key=GOOGLE_API_KEY)

def main(page: ft.Page):
    page.title = "Asistente Biblico"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True

    def buscar_palabra(_):
        try:
            palabra = input_palabra.value
            file = open(f"{palabra}.txt", "w", encoding="utf-8")
            significado = modelo.generate_content(f"¿Que significaba {palabra} en el diccionario?").text
            significado_original = modelo.generate_content(f"¿En la biblia en el lenguaje original que palabras se utilizaban para referirse a {palabra} y que significaba cada una?").text

            versos = modelo.generate_content(f"¿En que partes de la biblia se habla de {palabra}?").text
            ejemplo = modelo.generate_content(f"¿Que personajes biblicos son ejemplos de: {palabra}?").text
            comentarios = modelo.generate_content(f"¿Genera reflexiones muy profundas e intelectuales desde un punto de vista teologico sobre: {palabra}?").text

            bosquejo = modelo.generate_content(f"Haz un bosquejo con 5 ideas principales de {palabra} tomando en cuenta las siguientes conclusiones: {significado} \n\n {significado_original} \n\n {versos} \n\n {ejemplo} \n\n {comentarios}").text
            palabra_resultado.value = (f"La palabra {palabra} en el diccionario es: {significado} \n\n Yendonos a la etimología es: {significado_original} \n\n versos en los que se habla de ella: {versos} \n\n ejemplos biblicos de ella: {ejemplo} \n\n reflexiones: {comentarios} \n\n\n\n {bosquejo}")
            page.update()
            file.write(palabra_resultado.value)
        except Exception as e:
            print(f"Error: {e}")
            palabra_resultado.value = "Error al buscar la palabra. Por favor, inténtelo de nuevo."
            page.update()

    def buscar_versiculo(_):
        try:
            versiculo = input_versiculo.value
            file = open(f"{versiculo}.txt", "w", encoding="utf-8")
            texto = modelo.generate_content(f"¿Que dice {versiculo} en la biblia?").text
            relacionados = modelo.generate_content(f"¿Que versiculos de relacionan con: {versiculo}?").text
            comentarios = modelo.generate_content(f"¿Genera reflexiones muy profundas e intelectuales desde un punto de vista teologico sobre: {versiculo}?").text
            etimologia = modelo.generate_content(f"Toma la o las palabras que se consideren importantes y toma la palabra que se usaba en los lenguajes originales y da una descripcion de para que se usaba en {versiculo}?").text
            bosquejo = modelo.generate_content(f"Haz un bosquejo de {versiculo} tomando en cuenta las siguientes conclusiones: {etimologia} \n\n {texto} \n\n {relacionados} \n\n {comentarios}").text
            versiculo_resultado.value =  (f"El versiculo {versiculo} en la biblia dice: {texto} \n\n Palabras importantes en lenguas originales {etimologia}  \n\n Los versiculos relacionados son: {relacionados} \n\n reflexiones: {comentarios} \n\n\n\n {bosquejo}")
            page.update()
            file.write(versiculo_resultado.value)
        except Exception as e:
            print(f"Error: {e}")
            versiculo_resultado.value = "Error al buscar el versículo. Por favor, inténtelo de nuevo."
            page.update()

    def buscar_personaje(_):
        try:
            personaje = input_personaje.value
            file = open(f"{personaje}.txt", "w", encoding="utf-8")
            texto = modelo.generate_content(f"¿Quien fue {personaje} en la biblia (descripcion breve de lo que hizo)?").text
            versos = modelo.generate_content(f"¿En que partes de la biblia se habla de {personaje}?").text
            virtudes = modelo.generate_content(f"¿Cuales son las virtudes de {personaje} de la biblia?").text
            dificultades = modelo.generate_content(f"¿Cuales fueron las dificultades de {personaje} de la biblia?").text
            historia = modelo.generate_content(f"¿En que contexto historico vivio (que haya influido directamente en su historia) {personaje} de la biblia?").text
            bosquejo = modelo.generate_content(f"Haz un bosquejo con 5 ideas principales, que pueda ayudar a un predicador a preparar un sermon de {personaje} tomando en cuenta las siguientes conclusiones: {texto} \n\n {versos} \n\n {virtudes} \n\n {dificultades} \n\n {historia}").text
            personaje_resultado.value = (f"{texto} \n\n versos en los que se menciona: {versos} \n\n virtudes: {virtudes} \n\n dificultades: {dificultades} \n\n Contexto historico: {historia} \n\n\n\n {bosquejo}")
            page.update()
            file.write(personaje_resultado.value)
        except Exception as e:
            print(f"Error: {e}")
            buscar_personaje("")
            personaje_resultado.value = "Error al buscar el personaje"
            page.update()
    def palabra(_):
        page.clean()
        page.add(
            ft.Text("Asistente biblico", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Row(
                [
                    ft.ElevatedButton("Palabra", on_click=palabra),
                    ft.ElevatedButton("Versiculo", on_click=versiculo),
                    ft.ElevatedButton("Personaje", on_click=personaje),
                ],
                alignment=ft.MainAxisAlignment.CENTER
                
            )
        )
        page.add(
        ft.Text("Busqueda por Palabra", size=20, weight=ft.FontWeight.BOLD),
        input_palabra,
        ft.TextButton("Buscar por palabra", on_click=buscar_palabra),
        palabra_resultado
        )
        page.update()
    def versiculo(_):
        page.clean()
        page.add(
            ft.Text("Asistente biblico", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Row(
                [
                    ft.ElevatedButton("Palabra", on_click=palabra),
                    ft.ElevatedButton("Versiculo", on_click=versiculo),
                    ft.ElevatedButton("Personaje", on_click=personaje),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.add(
        ft.Text("Busqueda por Versiculo", size=20, weight=ft.FontWeight.BOLD),
        input_versiculo,
        ft.TextButton("Buscar por Versiculo", on_click=buscar_versiculo),
        versiculo_resultado
        )
        page.update()
    def personaje(_):
        page.clean()
        page.add(
            ft.Text("Asistente biblico", size=20, weight=ft.FontWeight.BOLD,),
            ft.Row(
                [
                    ft.ElevatedButton("Palabra", on_click=palabra),
                    ft.ElevatedButton("Versiculo", on_click=versiculo),
                    ft.ElevatedButton("Personaje", on_click=personaje),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.add(
        ft.Text("Busqueda por Personaje", size=20, weight=ft.FontWeight.BOLD),
        input_personaje,
        ft.TextButton("Buscar por personaje", on_click=buscar_personaje),
        
        personaje_resultado
        )
        page.update()
    page.title = "Asistente biblico"
    page.add(
        ft.Text("Asistente biblico", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
        ft.Row(
            [
                ft.ElevatedButton("Palabra", on_click=palabra),
                ft.ElevatedButton("Versiculo", on_click=versiculo),
                ft.ElevatedButton("Personaje", on_click=personaje),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
palabra_resultado = ft.Text("Resultados de la palabra")
versiculo_resultado = ft.Text("Resultados del versiculo")
personaje_resultado = ft.Text("Resultados del personaje")
input_personaje = ft.TextField(label="Personaje", width=300)
input_palabra = ft.TextField(label="Palabra", width=300)
input_versiculo = ft.TextField(label="Versiculo", width=300)


ft.app(target=main)