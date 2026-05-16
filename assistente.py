import os
from google import genai

def iniciar_assistente():
    nome_assistente = "Lumina"
    
    # ⚠️ REGRA DE OURO: Cole a sua chave do AI Studio entre as aspas abaixo
    Sua_API_KEY = "AIzaSyDhxJPktlcfr3rwFTdF4QE8AbY28mjGejM"
    
    # Configurando o cliente da IA
    client = genai.Client(api_key=MINHA_API_KEY)
    
    print(f"🤖 {nome_assistente}: Olá! Agora eu sou uma IA oficial.")
    print("Pode me perguntar qualquer coisa! (Digite 'sair' para encerrar)\n")
    
    while True:
        comando = input("Você: ").strip()
        
        if comando.lower() == "sair":
            print(f"\n🤖 {nome_assistente}: Até logo!")
            break
            
        if not comando:
            continue
            
        try:
            # Enviando a sua pergunta diretamente para o modelo Gemini 2.5 Flash
            resposta = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=comando,
            )
            
            # Exibindo a resposta inteligente na tela
            print(f"\n🤖 {nome_assistente}: {resposta.text}\n")
            
        except Exception as e:
            print(f"\n🤖 {nome_assistente}: Ops, tive um problema para me conectar. Erro: {e}\n")

if __name__ == "__main__":
    iniciar_assistente()
