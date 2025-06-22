# 🚗 CarFuture Shop

**CarFuture Shop** é um sistema web em desenvolvimento para gestão de revenda de carros.  
O projeto visa ser uma plataforma moderna, prática e visualmente agradável para cadastro e exibição de veículos disponíveis para venda.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Django](https://img.shields.io/badge/Framework-Django-092E20?logo=django)
![Made with Love](https://img.shields.io/badge/feito%20com-%E2%9D%A4-red)

---

## 📌 Funcionalidades atuais

- [x] Interface responsiva com tema escuro moderno 🌙  
- [x] Cadastro de veículos com:
  - Modelo, marca, ano de fabricação/modelo
  - Placa do carro (com validação)
  - Valor formatado com máscara de R$
  - Upload de imagem com preview antes do envio
- [x] Navegação entre páginas: lista de carros e formulário de cadastro

---

## 🛠️ Tecnologias utilizadas

- **Back-end**: [Django](https://www.djangoproject.com/)
- **Front-end**: HTML5 + CSS3 (Dark UI), JS Vanilla
- **Template Engine**: Django Templates + [widget-tweaks](https://github.com/jazzband/django-widget-tweaks)
- **Banco de Dados**: SQLite (por enquanto)
- **Ambiente virtual**: Python 3.11+ com venv

---

## 📦 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/carfuture-shop.git
cd carfuture-shop

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações e inicie o servidor
python manage.py migrate
python manage.py runserver
