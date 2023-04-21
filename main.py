import flet as ft
import openai
import sys,asyncio



def chatbot(peticion):
    try:
        openai.api_key = "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"
    except KeyError:
        sys.stderr.write("""
        We have a problem...
        """)
        exit(1)
    response = openai.Completion.create(
    model="gpt-3.5",
    prompt=peticion,
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    respuesta=response["choices"][0]["text"]
    return respuesta

def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField()

    def response(prompts):
        try:
            return(chatbot(prompts))
        except:
            print("Hemo tenido un error")

    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        chat.controls.append(ft.Text(chatbot(new_message.value)))

        #print(type(new_message.value))
        #await print(chatbot(new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )

ft.app(target=main)