# 💰 Controle de Gastos CLI

Sistema de controle de gastos desenvolvido em Python para gerenciamento financeiro simples via terminal.

## 📖 Descrição

O projeto permite cadastrar, listar, remover gastos e calcular o valor total das despesas registradas.

Nesta versão final, a aplicação foi integrada a um banco de dados PostgreSQL hospedado no Supabase, garantindo persistência dos dados em nuvem.

---

## 👥 Integrantes

| Nome | Matrícula |
|--------|------------|
| Márcia Kamyla Melo Ramos Castro | 22504647 |
| Inácio Barros de Sousa | 22509716 |

---

## 🚀 Tecnologias Utilizadas

- Python 3
- PostgreSQL
- Supabase
- Pytest
- GitHub Actions
- Git
- GitHub

---

## 📂 Estrutura do Projeto

```text
controle-gastos-cli/
│
├── src/
│   ├── main.py
│   ├── banco.py
│   └── cotacao.py
│
├── tests/
│   ├── test_api.py
│   ├── test_banco.py
│   └── test_gastos.py
│
├── .github/
├── .gitignore
├── requirements.txt
└── README.md
