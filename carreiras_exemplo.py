"""
Base simples de carreiras do futuro para o sistema de orientação.
Cada carreira possui:
- nome
- descricao
- trilha_aprendizado: lista de etapas sugeridas
- competencias_relevantes: dict com pesos (importância de 0 a 1)
- foco_futuro: pequeno resumo do impacto da carreira
"""

CARREIRAS_EXEMPLO = [
    {
        "nome": "Cientista de Dados",
        "descricao": "Profissional que extrai valor de grandes volumes de dados para apoiar decisões estratégicas.",
        "trilha_aprendizado": [
            "Fundamentos de programação (Python)",
            "Estatística e probabilidade",
            "Banco de dados e SQL",
            "Machine Learning",
            "Visualização de dados e storytelling",
        ],
        "competencias_relevantes": {
            "logica_programacao": 1.0,
            "dados_analise": 1.0,
            "ia_aprendizado": 0.7,
            "comunicacao": 0.5,
            "colaboracao": 0.4,
        },
        "foco_futuro": "Decisões orientadas a dados em diferentes setores.",
    },
    {
        "nome": "Engenheiro de IA",
        "descricao": "Profissional que projeta, treina e implementa modelos de inteligência artificial.",
        "trilha_aprendizado": [
            "Lógica de programação avançada",
            "Estruturas de dados e algoritmos",
            "Redes neurais e deep learning",
            "MLOps e deploy de modelos",
        ],
        "competencias_relevantes": {
            "logica_programacao": 1.0,
            "ia_aprendizado": 1.0,
            "dados_analise": 0.8,
            "adaptabilidade": 0.6,
        },
        "foco_futuro": "Criação de sistemas inteligentes que automatizam e ampliam capacidades humanas.",
    },
    {
        "nome": "UX Designer para Produtos Digitais",
        "descricao": "Profissional que projeta experiências digitais focadas nas necessidades reais das pessoas.",
        "trilha_aprendizado": [
            "Fundamentos de design e usabilidade",
            "Pesquisa com usuários",
            "Prototipação (Figma, etc.)",
            "Testes de usabilidade e iteração contínua",
        ],
        "competencias_relevantes": {
            "criatividade": 1.0,
            "comunicacao": 0.8,
            "colaboracao": 0.7,
            "adaptabilidade": 0.5,
        },
        "foco_futuro": "Construção de interfaces inclusivas e centradas no humano.",
    },
    {
        "nome": "Agile Project Leader",
        "descricao": "Profissional que lidera times multidisciplinares em ambientes ágeis.",
        "trilha_aprendizado": [
            "Fundamentos de gestão de projetos",
            "Scrum, Kanban e métodos ágeis",
            "Liderança servidora e facilitação",
            "Comunicação e resolução de conflitos",
        ],
        "competencias_relevantes": {
            "colaboracao": 1.0,
            "comunicacao": 0.9,
            "adaptabilidade": 0.8,
            "criatividade": 0.4,
        },
        "foco_futuro": "Liderança de equipes em ambientes complexos e em constante mudança.",
    },
    {
        "nome": "Especialista em Automação e RPA",
        "descricao": "Profissional focado em automatizar processos repetitivos com robôs de software.",
        "trilha_aprendizado": [
            "Mapeamento de processos de negócio",
            "Linguagens de script (ex: Python)",
            "Ferramentas de RPA",
            "Integração com sistemas legados",
        ],
        "competencias_relevantes": {
            "logica_programacao": 1.0,
            "adaptabilidade": 0.8,
            "colaboracao": 0.6,
        },
        "foco_futuro": "Automação inteligente para liberar tempo das pessoas para atividades de maior valor.",
    },
]
