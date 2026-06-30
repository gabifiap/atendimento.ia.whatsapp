from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from assistente import criar_chat

conversas = {}
app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    mensagem_cliente = form.get("Body", "")
    numero_cliente = form.get("From", "desconhecido")

    if numero_cliente not in conversas:
        conversas[numero_cliente] = criar_chat()

    chat = conversas[numero_cliente]
    resposta = chat.send_message(mensagem_cliente)
    texto_resposta = resposta.text

    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{texto_resposta}</Message>
</Response>"""

    return PlainTextResponse(content=twiml, media_type="application/xml")