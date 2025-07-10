# 💻 Sistema de Loja de Jogos

Este é um projeto acadêmico desenvolvido em Python utilizando o padrão MVC, com interface gráfica feita em Tkinter e banco de dados MongoDB. Trata-se de um sistema simples de loja de jogos, com funcionalidades completas e validações de entrada.

## 📋 Funcionalidades

O sistema possui 6 telas principais:

- **Início**: Tela inicial do sistema.
- **Catálogo**: Exibe a lista de jogos disponíveis para compra.
- **Carrinho**: Mostra os jogos adicionados e permite finalizar a compra.
- **Histórico**: Exibe o histórico de compras realizadas.
- **Adição de Jogos**: Permite adicionar novos jogos ao sistema.
- **Adição/Visualização de Saldo**: Permite adicionar saldo à conta e visualizar o saldo atual.

Todas as telas são funcionais e contam com **validações**:
- Campos obrigatórios não podem ficar em branco.
- Valores numéricos (como preço e saldo) não aceitam letras ou símbolos incorretos.
- Mensagens de erro são exibidas em caso de entradas inválidas.

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (Interface gráfica)
- **MongoDB** (Banco de dados)
- **MongoDB Compass** ou **MongoDB Atlas** para conexão e visualização dos dados.

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Instale o driver do MongoDB para Python.
3. Configure a conexão com o MongoDB local (Compass) ou remoto (Atlas).
4. Execute o projeto com: **python main.py**

## 📂 Estrutura do Projeto

O projeto segue a arquitetura MVC (Model-View-Controller), separando bem a lógica de controle, as telas (views) e os dados.

## 🎓 Sobre

Este projeto foi desenvolvido por Otavio Marcondes Ramalho como parte da disciplina Construção de Aplicações em Ambientes Virtuais do curso de Análise e Desenvolvimento de Sistemas, com foco em práticas de interface gráfica, persistência de dados e organização em camadas.
