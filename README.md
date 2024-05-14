### English README.md

**TorbTerm: An AI-Powered Terminal Assistant**

TorbTerm is a terminal-based AI assistant powered by Google's Gemini model. It allows you to interact with your operating system using natural language, making terminal tasks easier and more intuitive.

#### Features

- **Natural Language Interaction:** Issue commands to your terminal using natural language instead of memorizing complex syntax.
- **Cross-Platform Compatibility:** Works on macOS, Windows, and Linux.
- **System-Specific Shell Support:** Automatically uses the appropriate shell for your operating system (zsh, PowerShell, or bash).
- **Contextual Conversation:** Maintains a history of your interactions for more relevant responses.

#### Getting Started

**Prerequisites**

- Google AI Platform Account: You'll need an account on Google AI Platform.
- Google API Key: Obtain your API key from the AI Platform Console.
- Python 3.7 or higher
- `google-generativeai` Library: Install using `pip install google-generativeai`

**Set up API Key:**

1. Create a `.env` file in the same directory as the code files.
2. In the `.env` file, add your API key in the following format:
   ```
   GOOGLE_API_KEY="your_api_key"
   ```

**Install Dependencies:**

1. Navigate to the project directory in your terminal.
2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

**Run TorbTerm:**

Execute the Python script:
```bash
python torbterm.py
```

**Interact with the Assistant:**

Type your natural language instructions in the terminal.

TorbTerm will process your requests, execute commands, and provide responses.

#### How to Get a Google API Key

1. Go to Google AI Platform: Visit the [Google AI Platform](https://cloud.google.com/ai-platform).
2. Sign in or create an account.
3. Navigate to the AI Platform Console: Go to the AI Platform Console to manage your API credentials.
4. Create a new API key:
   - Click on "Create Credentials" and select "API key."
   - Copy the generated API key.

#### Examples

```
You: what is the current directory?
Torbware Assistant: @@pwd@@

You: create a new folder named "my_project"
Torbware Assistant: @@mkdir my_project@@

You: list all files in this directory
Torbware Assistant: @@ls -l@@
```

### Portuguese README.md

**TorbTerm: Um Assistente de Terminal com IA**

TorbTerm é um assistente de terminal baseado em IA, desenvolvido com o modelo Gemini do Google. Ele permite que você interaja com o seu sistema operacional usando linguagem natural, tornando as tarefas do terminal mais fáceis e intuitivas.

#### Recursos

- **Interação em Linguagem Natural:** Emita comandos para o seu terminal usando linguagem natural em vez de memorizar sintaxe complexa.
- **Compatibilidade entre Plataformas:** Funciona em macOS, Windows e Linux.
- **Suporte a Shell Específico do Sistema:** Usa automaticamente o shell apropriado para o seu sistema operacional (zsh, PowerShell ou bash).
- **Conversa Contextual:** Mantém um histórico das suas interações para respostas mais relevantes.

#### Como Começar

**Pré-requisitos**

- Conta Google AI Platform: Você precisará de uma conta no Google AI Platform.
- Chave de API do Google: Obtenha sua chave de API no Console do AI Platform.
- Python 3.7 ou superior
- Biblioteca `google-generativeai`: Instale usando `pip install google-generativeai`

**Configurar a Chave de API:**

1. Crie um arquivo `.env` no mesmo diretório dos arquivos de código.
2. No arquivo `.env`, adicione sua chave de API no seguinte formato:
   ```
   GOOGLE_API_KEY="sua_chave_de_api"
   ```

**Instalar Dependências:**

1. Navegue até o diretório do projeto no seu terminal.
2. Instale as bibliotecas necessárias:
   ```
   pip install -r requirements.txt
   ```

**Executar TorbTerm:**

Execute o script Python:
```bash
python torbterm.py
```

**Interagir com o Assistente:**

Digite suas instruções em linguagem natural no terminal.

TorbTerm processará suas solicitações, executará comandos e fornecerá respostas.

#### Como Obter uma Chave de API do Google

1. Acesse o Google AI Platform: Visite o [Google AI Platform](https://cloud.google.com/ai-platform).
2. Faça login ou crie uma conta.
3. Navegue até o Console do AI Platform: Acesse o Console do AI Platform para gerenciar suas credenciais de API.
4. Crie uma nova chave de API:
   - Clique em "Criar Credenciais" e selecione "Chave de API."
   - Copie a chave de API gerada.

#### Exemplos

```
Você: qual é o diretório atual?
Torbware Assistant: @@pwd@@

Você: crie uma nova pasta chamada "meu_projeto"
Torbware Assistant: @@mkdir meu_projeto@@

Você: liste todos os arquivos neste diretório
Torbware Assistant: @@ls -l@@
```
