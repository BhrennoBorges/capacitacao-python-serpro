# Nivelamento Técnico - Fundamentos de Python 🐍

Repositório criado para documentar e armazenar os exercícios práticos desenvolvidos durante as semanas de nivelamento técnico para o estágio. O foco foi dominar a sintaxe da linguagem, estruturas de controle, tratamento de erros, manipulação de coleções e automação de sistemas através do livro *"Automatize Tarefas Maçantes com Python"*.

---

## 📅 Diário de Bordo - 08/06/2026

Nesta etapa, finalizei a leitura e a implementação prática dos **Capítulos 1 ao 5**. Todos os scripts foram testados, corrigidos contra erros de indentação/tipagem e encontram-se 100% funcionais.

### 📝 Resumo dos Capítulos e Scripts Desenvolvidos:

* **Capítulo 1: Fundamentos de Python (`hello.py`)**
    * **O que aprendi:** Manipulação básica de strings, armazenamento de dados em variáveis e o uso das funções essenciais `input()`, `print()` e `len()`. Compreendi como a conversão de tipos (`str()`, `int()`) evita falhas de execução.
* **Capítulo 2: Controle de Fluxo (`guessTheNumber.py`)**
    * **O que aprendi:** Uso de blocos condicionais (`if`, `elif`, `else`) e loops de repetição (`for` combinado com `range()`). Aprendi a usar o comando `break` para interromper laços e a importância crucial da indentação correta em Python.
* **Capítulo 3: Funções (`collatz.py`)**
    * **O que aprendi:** Como organizar e reutilizar blocos de código definindo funções com `def`, passando argumentos e capturando retornos com `return`. Implementei também a blindagem de segurança com os blocos `try` e `except ValueError` para evitar travamentos por dados inválidos do usuário.
* **Capítulo 4: Listas (`commaCode.py`)**
    * **O que aprendi:** Manipulação de coleções ordenadas de dados (`list`). Desenvolvi uma lógica de indexação para identificar dinamicamente a posição dos elementos (iterações normais, penúltimo e último item) para formatação de strings complexas.
* **Capítulo 5: Dicionários (`inventory.py`)**
    * **O que aprendi:** Estruturação de dados no formato de Chave-Valor (`dict`). Utilizei métodos utilitários como o `.items()` para percorrer dicionários com laços de repetição e o uso estratégico da palavra-chave `pass` como placeholder de escopo.

---

## 📅 Diário de Bordo - 10/06/2026 (Postado em 11/06/2026)

Finalizei o estudo avançado e a implementação prática dos **Capítulos 6 ao 11**. Este bloco foi focado no desenvolvimento de scripts voltados para a automação de sistemas, auditoria de infraestrutura e cibersegurança, simulando rotinas reais do ambiente de desenvolvimento corporativo.

### 📝 Resumo dos Capítulos e Scripts Desenvolvidos:

* **Capítulo 6: Manipulação de Strings (`parser_logs.py`)**
    * **O que aprendi:** Higienização e tratamento de textos brutos. Utilizei métodos como `.strip()` para remoção de quebras de linha e espaços invisíveis, `.split()` para fatiamento de dados e f-strings estruturadas para transformar strings sujas em alertas padronizados de servidores.
* **Capítulo 7: Expressões Regulares (`extrator_ips.py`)**
    * **O que aprendi:** Construção de "moldes" avançados de busca por meio do módulo nativo `re`. Desenvolvi uma lógica de filtragem via `re.compile()` e `.findall()` capaz de varrer relatórios de rede extensos e extrair endereços IPv4 isolados de forma automatizada.
* **Capítulo 8: Validação de Dados de Entrada (`validador_portas.py`)**
    * **O que aprendi:** Blindagem de software contra falhas de digitação e dados corrompidos usando a biblioteca `PyInputPlus`. Implementei restrições de tipos numéricos com intervalos fechados (como limites de portas de rede de 1 a 65535) e validações booleanas de confirmação, mitigando erros em tempo de execução (*crashes*).
* **Capítulo 9: Leitura e Escrita de Arquivos (`gerenciador_whitelist.py`)**
    * **O que aprendi:** Persistência de dados locais utilizando a sintaxe segura `with open()`. Pratiquei a manipulação de arquivos físicos no disco rígido através dos modos de escrita (`'w'`) para criação de regras de acesso (whitelist) e leitura (`'r'`) para carregamento de informações em memória.
* **Capítulo 10: Organização de Arquivos (`organizador_arquivos.py`)**
    * **O que aprendi:** Automação de rotinas do sistema operacional utilizando os módulos `os` e `shutil`. Compreendi como verificar a existência de diretórios (`os.path.exists`), criar pastas automaticamente (`os.makedirs`) e gerenciar caminhos lógicos para cópias de segurança de arquivos de configuração.
* **Capítulo 11: Depuração / Debugging (`depurador_logs.py`)**
    * **O que aprendi:** Substituição de saídas informais de tela (`print`) por rastreamento profissional baseado no módulo `logging`. Aprendi a configurar níveis hierárquicos de criticidade (`DEBUG`, `INFO`, `ERROR`) direcionados para arquivos físicos de auditoria (`.log`), capturando anomalias operacionais de forma silenciosa e rastreável.

---

## 🚀 Prática de Git & Evolução do Fluxo de Trabalho

Aproveitei a construção deste repositório para praticar o uso do Git diretamente pelo terminal integrado do VS Code, aprimorando o controle de versão em duas etapas fundamentais:

### Etapa 1: Comandos Essenciais (08/06)
O objetivo inicial foi fixar os comandos base de empacotamento e envio:
* **`git status`**: Mapeamento de arquivos modificados.
* **`git add`**: Movimentação de arquivos para a área de preparação (*Staging Area*).
* **`git commit`**: Registro local das alterações.
* **`git push`**: Envio do pacote para o repositório remoto.

### Etapa 2: Commits Atômicos e Sincronização (11/06)
A utilização do Git foi aprofundada para refletir boas práticas reais de ambientes de produção:
* **Commits Atômicos**: Em vez de unificar múltiplos arquivos em um único envio genérico, cada script foi preparado de forma cirúrgica (`git add [arquivo]`) e registrado com sua própria mensagem semântica descritiva.
* **Resolução de Divergências (`git pull` & Merge)**: Sincronização da branch local com o repositório remoto utilizando `git pull origin main --allow-unrelated-histories` para mesclar históricos divergentes de forma segura.
* **Uso de Editores por Terminal (Vim)**: Prática dos comandos essenciais de console (como o atalho de salvamento e fechamento `:wq`) para concluir mensagens de mesclagem diretamente no terminal antes do envio definitivo.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 3
* **Ambiente de Desenvolvimento:** Visual Studio Code (VS Code)
* **Controle de Versão:** Git & GitHub

---
*Progresso documentado entre os dias 08 e 11 de junho de 2026.*
