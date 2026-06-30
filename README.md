# Chatbot de Atendimento via WhatsApp com IA

Assistente virtual de atendimento ao cliente desenvolvido para funcionar diretamente no WhatsApp, sem aplicativo adicional. O cliente manda uma mensagem e recebe uma resposta instantânea, como se estivesse falando com um atendente real.

**Teste agora:** escaneie o QR code abaixo ou mande "join advice-related" para o número +1 415 523 8886 no WhatsApp.

> ⚠️ Por ser um ambiente de testes (Twilio Sandbox), é necessário enviar esse código uma vez antes de começar a conversar. Depois disso, é só mandar sua dúvida normalmente.

<img width="218" height="214" alt="image" src="https://github.com/user-attachments/assets/4c4f2a99-6a18-45ee-b703-93f5723be412" />


## Sobre o projeto

O modelo foi treinado para atender uma confeitaria — respondendo dúvidas sobre disponibilidade de produtos, opções sem glúten, formas de pagamento, frete, trocas e situações mais delicadas como pedidos errados ou clientes insatisfeitos.

Mas o ponto principal não é o nicho: **o mesmo sistema pode ser adaptado para qualquer tipo de negócio**. Clínica, barbearia, loja de roupas, escritório de advocacia — o que muda é só o conteúdo do modelo. A estrutura de funcionamento permanece a mesma.

## Como foi construído

A personalidade e o comportamento do assistente foram definidos por mim através de um Modelfile e um dataset de conversas reais do nicho, cobrindo situações comuns de atendimento: perguntas frequentes, reclamações, pedidos de reembolso e escalada para atendimento humano. Esse material foi usado para modelar como a IA responde, com qual tom e onde ela deve ou não tomar decisões sozinha.

A integração com o WhatsApp foi feita via Twilio, que recebe as mensagens do cliente e as encaminha para o servidor. O servidor processa a mensagem, consulta o modelo de linguagem (Google Gemini) e devolve a resposta para a Twilio entregar ao cliente — tudo em segundos.

O backend foi desenvolvido em Python com FastAPI.

## Stack

- Python + FastAPI
- Google Gemini (modelo de linguagem)
- Twilio WhatsApp API
- Modelfile + dataset próprio para treinamento do comportamento

## Como testar localmente

```bash
git clone https://github.com/gabifiap/chatbot-whatsapp-ia.git
cd chatbot-whatsapp-ia
python -m venv venv
.\venv\Scripts\Activate  # Windows
pip install -r requirements.txt
```

Crie um arquivo `.env` com suas credenciais:

```
TWILIO_ACCOUNT_SID=seu_sid
TWILIO_AUTH_TOKEN=seu_token
GEMINI_API_KEY=sua_chave
```

```bash
uvicorn main:app --reload
```

Configure o webhook da Twilio Sandbox apontando para `https://seu-ngrok.ngrok-free.app/webhook`.

## Próximos passos

- Memória de conversa persistente entre sessões (hoje o histórico existe dentro de uma sessão, mas reinicia se o servidor for restarted)
- Painel simples pra o dono do negócio visualizar as conversas
- Integração com número WhatsApp Business aprovado pela Meta

---

Desenvolvido por Gabriela Batista.
