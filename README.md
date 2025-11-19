# Global Solution 2025.2 – Sistema de Orientação de Carreiras do Futuro

Disciplina: **Pensamento Computacional e Automação com Python**  
Curso: Ciência da Computação – 1º ano  
Professor: Alexandre Russi Jr.
Sala: 1CCA
Integrantes:
  - Luiz Miguel Martin Crocco - RM: 562796
  - Rafael Louzã Lopes - RM: 564963

## 1. Descrição do Projeto

Este projeto implementa um **sistema em Python orientado a objetos** que simula uma
ferramenta inteligente de orientação de carreiras para o **trabalho do futuro**,
alinhado ao tema *Future at Work* e ao contexto do **Future Skills Lab**.  

O sistema:

- Organiza perfis profissionais com base em competências técnicas e comportamentais;
- Analisa essas competências;
- Gera recomendações de **carreiras do futuro**, trilhas de aprendizado e pontos de melhoria.

As principais competências consideradas incluem:

- Lógica de programação;
- Criatividade;
- Colaboração;
- Adaptabilidade;
- Comunicação;
- Interesse por dados;
- Interesse por IA e aprendizado contínuo.

## 2. Estrutura de Arquivos

```text
.
├── main.py                     # Interface textual (CLI) do sistema
├── models
│   ├── __init__.py
│   ├── perfil.py               # Classe Perfil
│   ├── carreira.py             # Classe Carreira
│   └── recomendador.py         # Classe Recomendador
├── data
│   └── carreiras_exemplo.py    # Base de carreiras do futuro (listas/dicionários)
└── README.md                   # Este arquivo
```

## 3. Conceitos de Programação Utilizados

- **Orientação a Objetos (OOP)**
  - Classes: `Perfil`, `Carreira`, `Recomendador`;
  - Atributos e métodos bem definidos;
  - Uso de `dataclasses` para simplificar o modelo.

- **Estruturas de dados**
  - **Listas**: lista de carreiras, lista de trilhas de aprendizado;
  - **Dicionários**: competências do perfil, competências relevantes de cada carreira;
  - **Tuplas** podem ser utilizadas em extensões da aplicação (ex: pares `(carreira, score)`).

- **Lógica e condicionais**
  - Cálculo de score de aderência entre perfil e cada carreira;
  - Identificação de competências a desenvolver.

- **Automação**
  - Geração automática de recomendações com base nos dados fornecidos;
  - Exportação de resumo para arquivo `.txt`.

## 4. Como Executar

Pré-requisitos:

- Python 3.10+ instalado.

Passos:

1. Clonar o repositório ou extrair os arquivos do projeto;
2. No terminal, entrar na pasta do projeto;
3. Executar:

```bash
python main.py
```

## 5. Funcionalidades da Interface (CLI)

Ao executar `main.py`, o menu principal oferece:

- **1 – Cadastrar/atualizar perfil**  
  O usuário informa nome, RM (opcional) e autoavalia suas competências de 0 a 10.

- **2 – Listar carreiras do futuro disponíveis**  
  Exibe as carreiras cadastradas na base de dados.

- **3 – Gerar recomendações para o perfil atual**  
  Mostra as carreiras mais aderentes ao perfil, indicando:
  - Aderência percentual;
  - Descrição da carreira;
  - Trilha de aprendizado sugerida;
  - Competências que ainda precisam ser fortalecidas.

- **4 – Exportar resumo do perfil e recomendações**  
  Gera um arquivo `resumo_perfil_carreiras.txt` com:
  - Dados do perfil;
  - Competências avaliadas;
  - Top 3 recomendações com trilhas de aprendizado.

- **0 – Sair**  
  Encerra o sistema.

## 6. Conexão com o Tema Future at Work

O projeto está alinhado com o tema **Future at Work** porque:

- Aborda carreiras emergentes como Cientista de Dados, Engenheiro de IA, UX Designer e Especialista em Automação;
- Enfatiza competências humanas essenciais para o futuro, como adaptabilidade, colaboração e comunicação;
- Demonstra como a **automação** (no caso, um recomendador em Python) pode apoiar o desenvolvimento humano, em vez de substituí-lo;
- Estimula o aluno a refletir sobre seu próprio perfil e possíveis caminhos profissionais.
