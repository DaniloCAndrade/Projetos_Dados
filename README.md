# 📊 Projetos de Análise de Dados - EBAC

Repositório de projetos realizados ao longo do curso de **Analista de Dados** da [EBAC]. Aqui você encontrará uma coleção de scripts, notebooks e soluções práticas que combinam **Python**, **análise de dados** e outras ferramentas de dados.

---

## 📁 Estrutura do Repositório

---

## ✅ Projeto 1: Calculadora Inteligente (projeto_1_calc)

Uma calculadora básica — mas com alma! Criada com **Python puro**, rodável via **script .sh no Ubuntu**, e com repetição de operações até o usuário desejar sair.

### 🛠️ Tecnologias utilizadas:
- Python 3.8+
- Shell Script (Bash)
- Terminal Linux (Ubuntu)

### 📄 Arquivos principais:
- `calculadora.py` → Script principal com lógica da calculadora
- `calculadora.sh` → Script de automação para rodar o Python no Ubuntu

### 🔄 Funcionalidades do Código:
- Solicitação do nome do usuário na execução do código;
- Entrada de dois valores;
- Operações básicas: soma, subtração, multiplicação, divisão, potenciação;
- Loop com confirmação para continuar ou encerrar a calculadora;

### ▶️ Como executar:

```bash
# Se for a sua primeira execução, utilize o comando:
git clone caminho_do_projeto

# Acesse o diretório Projeto_Dados
cd Projeto_Dados

# Acesse o diretório do projeto
cd projeto_1_calc

# Dê permissão de execução ao script
chmod 744 calculadora.sh

# Execute a calculadora
./calculadora.sh
