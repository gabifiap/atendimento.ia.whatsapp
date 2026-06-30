from assistente import criar_chat

testes = [
    "Posso pagar com cartão fisico?",
    "Esqueceram as velas do aniversário!",
    "Tenho alergia a amendoim, o app avisa os restaurantes?",
    "Paguei pelo PIX e não confirmou.",
    "O endereço de entrega está errado, posso modificar após o pedido ser feito?",
    "O app não está me deixando concluir meu pedido, o que posso fazer?.",
    "Quero falar com um humano agora!"
]

chat = criar_chat()

print("=" * 60)
print("🧪 TESTES — GEMINI (gemini-2.5-flash)")
print("=" * 60)

for pergunta in testes:
    resposta = chat.send_message(pergunta)
    print(f"\n👤 {pergunta}")
    print(f"🤖 {resposta.text}")
    print("-" * 60)