import google.generativeai as genai
import subprocess
import platform
import os
from config import configure_api

configure_api()
print(genai.__version__)

# Dicionário de instruções do sistema por sistema operacional
system_instructions = {
    "Darwin": {
        "shell": "zsh",
        "instructions": lambda: f"""- Este modelo tem controle total sobre o terminal e o sistema operacional.
- O diretório atual é: {os.getcwd()}
- O conteúdo do diretório atual é: {os.listdir(os.getcwd())}
- Os comandos devem ser enviados entre @@ para serem executados no terminal.
- Certifique-se de fornecer comandos válidos e seguros.
- Evite comandos que exijam interação do usuário ou que possam causar danos ao sistema.
- Exemplos de comandos:
  - @@ls -l@@: Lista os arquivos e diretórios no diretório atual com detalhes.
  - @@pwd@@: Exibe o diretório de trabalho atual.
  - @@cat arquivo.txt@@: Exibe o conteúdo do arquivo especificado.
  - @@echo \"Olá, mundo!\"@@: Exibe a mensagem \"Olá, mundo!\" no terminal.
  - @@mkdir novo_diretorio@@: Cria um novo diretório com o nome especificado.
  - @@rm arquivo.txt@@: Remove o arquivo especificado.
  - @@mv arquivo.txt novo_nome.txt@@: Renomeia o arquivo especificado para o novo nome.
  - @@cp arquivo.txt pasta_destino/@@: Copia o arquivo especificado para a pasta de destino.
  - @@touch novo_arquivo.txt@@: Cria um novo arquivo com o nome especificado.
  - @@grep \"texto\" arquivo.txt@@: Procura por um texto específico no arquivo especificado."""
    },
    "Windows": {
        "shell": "powershell",
        "instructions": lambda: f"""- Este modelo tem controle total sobre o terminal e o sistema operacional.
- O diretório atual é: {os.getcwd()}
- O conteúdo do diretório atual é: {os.listdir(os.getcwd())}
- Os comandos devem ser enviados entre @@ para serem executados no terminal.
- Certifique-se de fornecer comandos válidos e seguros.
- Evite comandos que exijam interação do usuário ou que possam causar danos ao sistema.
- Exemplos de comandos:
  - @@Get-ChildItem -File@@: Lista os arquivos no diretório atual.
  - @@Get-Location@@: Exibe o diretório de trabalho atual.
  - @@Get-Content arquivo.txt@@: Exibe o conteúdo do arquivo especificado.
  - @@Write-Host \"Olá, mundo!\"@@: Exibe a mensagem \"Olá, mundo!\" no terminal.
  - @@New-Item -ItemType Directory -Name novo_diretorio@@: Cria um novo diretório com o nome especificado.
  - @@Remove-Item arquivo.txt@@: Remove o arquivo especificado.
  - @@Rename-Item -Path arquivo.txt -NewName novo_nome.txt@@: Renomeia o arquivo especificado para o novo nome.
  - @@Copy-Item -Path arquivo.txt -Destination pasta_destino/@@: Copia o arquivo especificado para a pasta de destino.
  - @@New-Item -ItemType File -Name novo_arquivo.txt@@: Cria um novo arquivo com o nome especificado.
  - @@Select-String -Pattern \"texto\" -Path arquivo.txt@@: Procura por um texto específico no arquivo especificado."""
    },
    "Linux": {
        "shell": "bash",
        "instructions": lambda: f"""- Este modelo tem controle total sobre o terminal e o sistema operacional.
- O diretório atual é: {os.getcwd()}
- O conteúdo do diretório atual é: {os.listdir(os.getcwd())}
- Os comandos devem ser enviados entre @@ para serem executados no terminal.
- Certifique-se de fornecer comandos válidos e seguros.
- Evite comandos que exijam interação do usuário ou que possam causar danos ao sistema.
- Exemplos de comandos:
  - @@ls -l@@: Lista os arquivos e diretórios no diretório atual com detalhes.
  - @@pwd@@: Exibe o diretório de trabalho atual.
  - @@cat arquivo.txt@@: Exibe o conteúdo do arquivo especificado.
  - @@echo \"Olá, mundo!\"@@: Exibe a mensagem \"Olá, mundo!\" no terminal.
  - @@mkdir novo_diretorio@@: Cria um novo diretório com o nome especificado.
  - @@rm arquivo.txt@@: Remove o arquivo especificado.
  - @@mv arquivo.txt novo_nome.txt@@: Renomeia o arquivo especificado para o novo nome.
  - @@cp arquivo.txt pasta_destino/@@: Copia o arquivo especificado para a pasta de destino.
  - @@touch novo_arquivo.txt@@: Cria um novo arquivo com o nome especificado.
  - @@grep \"texto\" arquivo.txt@@: Procura por um texto específico no arquivo especificado."""
    }
}

# Obtém o sistema operacional atual
current_os = platform.system()

# Obtém as instruções do sistema para o sistema operacional atual
current_instructions = system_instructions.get(current_os, system_instructions["Linux"])["instructions"]()

# Configurações de segurança
safety_settings = []

# Configurações de geração
generation_config = {
    "candidate_count": 1,
    "temperature": 0.2,
}

# Crie o modelo GenerativeModel com as configurações
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)

current_directory = os.getcwd()  # Inicializa com o diretório atual
chat_history = []  # Inicializa o histórico do chat

import os

def execute_command(command):
    """Executa um comando no sistema operacional atual."""
    global current_directory
    if command.startswith("cd "):
        try:
            new_dir = command.split("cd ")[1].strip()
            new_dir = os.path.expanduser(new_dir)  # Expande o ~ para o diretório home absoluto
            os.chdir(new_dir)
            current_directory = os.getcwd()  # Atualiza o diretório atual
            print(f"Diretório alterado para: {current_directory}")
        except FileNotFoundError:
            print(f"Diretório não encontrado: {new_dir}")
    else:
        try:
            subprocess.run([system_instructions[current_os]["shell"], "-c", command.strip()], check=True, cwd=current_directory)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar comando:", e)


def main():
    """Loop principal do programa."""
    global chat_history
    prompt = ""
    while prompt != "fim":
        prompt = input("Você: ")
        chat_history.append({"role": "user", "content": prompt})

        # Envia o histórico do chat para o modelo
        response = model.generate_content(
            contents=[{"role": "user", "parts": [{"text": message["content"] + "\nSistema: " + current_os + "\nShell: " + system_instructions[current_os]["shell"] + "\nInstruções: " + current_instructions} for message in chat_history]}]
        )

        # Extrai a resposta do modelo
        assistant_response = response.text
        print(f"Torbware Assistant: {assistant_response}\n")
        chat_history.append({"role": "assistant", "content": assistant_response})

        # Verifica se há comandos na resposta
        if '@' in assistant_response:
            commands = assistant_response.split('@')
            for command in commands:
                if command:  # Ignora strings vazias
                    execute_command(command)

if __name__ == "__main__":
    main()