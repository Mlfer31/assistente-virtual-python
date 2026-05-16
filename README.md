# Assistente Virtual com Inteligência Artificial - Lumina 🤖

Este é um projeto prático desenvolvido em Python no ambiente VS Code. O objetivo foi construir um assistente virtual interativo via terminal (em loop contínuo) e integrá-lo diretamente à API oficial do Gemini, transformando um script local em uma ferramenta conversacional inteligente.

## 🎯 Funcionalidades
* **Interface via Terminal:** Interação em tempo real com o usuário através de um loop de captura de dados.
* **Integração com IA:** Consumo da API do Google GenAI utilizando o modelo `gemini-2.5-flash` para responder a perguntas gerais, códigos e lógica.
* **Tratamento de Erros:** Resolução de problemas de ambiente, caminhos de execução no PowerShell e gerenciamento de dependências.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.14
* **SDK:** `google-genai`
* **Editor de Código:** VS Code
* **Terminal:** Windows PowerShell

## 🚀 Como Executar o Projeto

1. **Pré-requisitos:** Certifique-se de ter o Python instalado na sua máquina.
2. **Clonar o projeto:** Baixe o arquivo `assistente.py` para uma pasta de sua preferência.
3. **Instalar a biblioteca da API:** Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python -m pip install google-genai
