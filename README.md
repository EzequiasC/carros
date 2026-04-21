# 🚗 Carros — Sistema Web para Revenda de Veículos

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?logo=django)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Made by](https://img.shields.io/badge/made%20by-Ezequias%20Correa-blue)

---

## 📌 Sobre o Projeto

O **Carros** é uma aplicação web completa voltada para o gerenciamento de uma loja de veículos, permitindo a interação entre vendedores e compradores (*olheiros*).

O sistema simula um ambiente real de revenda automotiva, com controle de estoque, anúncios e gestão de usuários.

---

## 👥 Tipos de Usuário

### 👀 Olheiro (Comprador)

* Visualiza todos os veículos disponíveis
* Acessa detalhes completos dos carros
* Pode entrar em contato com vendedores
* Também possui acesso à listagem de estoque

### 💼 Vendedor

* Cadastra novos veículos
* Edita e remove anúncios
* Gerencia seu próprio estoque
* Visualiza todos os seus veículos cadastrados

---

## 🚀 Funcionalidades

* Sistema de autenticação de usuários
* Diferenciação de perfis (Olheiro / Vendedor)
* Cadastro de veículos com upload de imagens
* Edição e exclusão de anúncios
* Listagem de estoque
* Integração com API de cidades (IBGE)
* Validação de dados (ex: usuários duplicados)
* Manipulação de imagens com Pillow

---

## 🛠️ Tecnologias Utilizadas

* Python 3.13
* Django
* HTML5
* CSS
* Pillow
* API do IBGE (cidades)

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/EzequiasC/carros.git
cd carros
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Rode o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 🗂️ Estrutura do Projeto

```bash
carros/
│
├── accounts/        # Autenticação e usuários
├── app/             # Núcleo principal (lógica central)
├── cars/            # Gestão de veículos
├── sellers/         # Funcionalidades dos vendedores
├── media/           # Upload de imagens
│
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## 🌐 Integrações

* API pública do IBGE para busca de cidades

---

## 📷 Demonstração

> Em breve: imagens e demonstração do sistema

---

## 📄 Licença

Este projeto é destinado para fins acadêmicos e aprendizado.

---

## 👨‍💻 Autor

**Ezequias Correa**
🔗 https://github.com/EzequiasC

---
