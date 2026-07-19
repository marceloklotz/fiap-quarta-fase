# 👩‍⚕️👨‍💻 Inteligência Artificial Multimodal na Saúde da Mulher: Visão Computacional e Análise de Áudio

[![FIAP Postech em IA para Devs](https://img.shields.io/badge/FIAP-Postech%20IA%20para%20Devs-blue?style=for-the-badge)](https://www.fiap.com.br/)
[![Fase 4 - Tech Challenge](https://img.shields.io/badge/Fase_4-Tech_Challenge-purple?style=for-the-badge)](#)

Este repositório contém o código-fonte e as especificações técnicas desenvolvidos no âmbito do desafio (Tech Challenge) apresentado durante a **Quarta Fase da Pós Tech (8IADT)**, da **Faculdade de Informática e Administração Paulista (FIAP)**, conforme requisitos contidos no [PDF](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Desafio%20-%20Fase%204%20-%20Tech%20challenge%20Secretaria.pdf) disponível no presente repositório. O projeto propõe um ecossistema multimodal focado no suporte e na segurança da saúde da mulher, dividido em dois módulos principais: análise preditiva de vídeo intraoperatório e automação de prontuários via inteligência vocal e generativa.

<p align="center">
  <picture><img src="https://github.com/marceloklotz/fiap-quarta-fase/blob/main/assets/infografico.png" alt="Visão geral do projeto"></picture>
</p>

## ⚠️ Aviso de Uso Acadêmico e Isenção de Responsabilidade

> **IMPORTANTE:** Os componentes deste repositório foram desenvolvidos exclusivamente para fins educacionais, científicos e de demonstração de viabilidade tecnológica. 
> * **Não substituem validações médicas oficiais.**
> * **Não estão aptos para embasar decisões clínicas em tempo real, realizar diagnósticos ou apoiar triagens hospitalares.**
> * Toda e qualquer interpretação ou uso derivado deste código deve ficar estritamente sob a supervisão de profissionais de saúde competentes.

<picture>
  <img src="https://img.shields.io/badge/-ebebeb?style=for-the-badge&logoColor=black" width="100%" height="10px" alt="Integrantes do Grupo">
</picture>
  
## 👥 Integrantes do grupo
Os membros do grupo são compostos pelos seguintes servidores da **Secretaria de Segurança Pública do Distrito Federal (SSP/DF)**:

- Alexandre Natã Vicente (**rm370024**) (ale.n.vicente@gmail.com)
- Antônio Cláudio Almeida (**rm370052**) (antonioalmeida@gmail.com)
- Cyd Ferreira Rodrigues (**rm370004**) (cydnelson@gmail.com)
- David Catherink (**rm369997**) (d.catherinck@gmail.com)
- Marcelo Macedo Klotz (**rm370010**) (marceloklotz@gmail.com) 

<picture>
  <img src="https://img.shields.io/badge/-ebebeb?style=for-the-badge&logoColor=black" width="100%" height="10px" alt="Integrantes do Grupo">
</picture>

## 👥 Visão geral do projeto

<p align="center">
  <img src="https://github.com/marceloklotz/fiap-quarta-fase/blob/main/assets/sobre.gif" alt="Apresentação - Visão geral"> 
  <br><sub>Apresentação com a visão geral do projeto. Slides gerados via NkLM, com transição de 7 segundos.</sub>
</p>

<picture>
  <img src="https://img.shields.io/badge/-ebebeb?style=for-the-badge&logoColor=black" width="100%" height="10px" alt="Integrantes do Grupo">
</picture>

# 🚀 Componentes Principais

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](#)
[![YOLOv8](https://img.shields.io/badge/Ultralytics-YOLOv8-FF6F00?style=flat-square&logo=ultralytics&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](#)
[![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?style=flat-square&logo=openai&logoColor=white)](#)
[![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](#)
[![Amazon S3](https://img.shields.io/badge/Amazon_S3-AWS-232F3E?style=flat-square&logo=amazons3&logoColor=white)](#)
[![Librosa](https://img.shields.io/badge/Librosa-DSP-993333?style=flat-square)](#)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](#)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](#)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](#)
[![Hugging Face](https://img.shields.io/badge/🌿_Hugging_Face-Transformers-FFD21E?style=flat-square)](#)

O sistema combina capacidades multimodais de **Visão Computacional** e **Processamento de Sinais de Áudio** estruturando-se em dois módulos funcionais:

## 1. 🩸 Módulo Detecção de Sangramentos (Análise de Vídeo)
Desenvolvido para atuar no contexto macro de cirurgias ginecológicas por laparoscopia (cirurgias minimamente invasivas voltadas ao tratamento de endometriose, miomas, cistos ou gravidez ectópica).
* **Objetivo:** Monitorar o fluxo de vídeo e classificar em tempo real a ocorrência de anomalias cirúrgicas como o sangramento intraoperatório.
* **Abordagem Técnico-Científica:** Uma pipeline construída sobre o **YOLOv8** (modelo `yolov8n-cls.pt` ajustado por *fine-tuning*), que analisa os frames processados temporalmente via OpenCV. 
* **Lógica Antibumping / Flickering:** Implementação de uma mecânica de janela deslizante (*sliding window*). O sistema exige a predição consistente acima do limiar de confiança em $X$ frames consecutivos para disparar alertas visuais em formato de moldura vermelha, mitigando alarmes falsos para o cirurgião.

## 2. 🎙️ Módulo Atendimento Clínico (Análise de Áudio)
Uma solução *end-to-end* projetada para apoiar consultas de ginecologia ou obstetrícia a partir do áudio capturado na relação médico-paciente.
* **Processamento Digital de Sinais (DSP):** Extração local de biomarcadores acústicos (tom de voz e taxas de hesitação) sem dependência de nuvem, preservando a latência e a privacidade de dados sensíveis da paciente.
* **Transcrição Automatizada (ASR):** Emprego do modelo **OpenAI Whisper** de forma nativa para transcrição de áudio clínico de forma robusta e resistente a ruídos hospitalares de fundo.
* **Estruturação Cognitiva (LLM):** Integração via sintaxe declarativa **LCEL (LangChain Expression Language)** com Engenharia de Prompt Defensiva para traduzir, contextualizar termos técnicos e gerar automaticamente um prontuário médico estruturado no padrão internacional **SOAP** (Subjetivo, Objetivo, Avaliação e Plano).

# 🛠️ Detalhamento e Aplicação Prática das Tecnologias

Para garantir o funcionamento integrado e robusto do ecossistema multimodal, cada tecnologia e biblioteca desempenha um papel estratégico bem definido no código:

## 🩸 Módulo de Detecção de Sangramentos (Análise de Vídeo)

* **`ultralytics` (YOLOv8)**
  * **Onde é utilizada:** No treinamento, validação e execução do modelo preditivo.
  * **Aplicação prática:** Realiza o *fine-tuning* do modelo base `yolov8n-cls.pt` a partir das imagens do dataset *GynSurg* no notebook de treinamento (`MOD_Bleeding_Train_GPU.ipynb`). O arquivo final de pesos gerado (`best.pt`) é importado pelo script de inferência para classificar os frames cirúrgicos em tempo real.
* **`opencv-python` (cv2)**
  * **Onde é utilizada:** Nos scripts de manipulação de vídeo e engenharia de dados (`extract_frames.py` e `bleeding-detection.py`).
  * **Aplicação prática:** Responsável por ler o fluxo de vídeo frame a frame, redimensionar as imagens para os requisitos de entrada do modelo e implementar a mecânica de janela deslizante (*sliding window*). Também renderiza as sobreposições na tela, como a moldura vermelha de alerta visual quando anomalias consecutivas são detectadas.
* **`torch` (PyTorch)**
  * **Onde é utilizada:** Como o motor (*backend*) essencial de processamento matemático profundo.
  * **Aplicação prática:** Gerencia a alocação de memória e garante que os cálculos matemáticos do YOLOv8 utilizem aceleração por hardware (GPU/CUDA), viabilizando taxas de FPS altas e compatíveis com procedimentos cirúrgicos reais.
* **`awscli` (Amazon S3)**
  * **Onde é utilizada:** Na automação da infraestrutura de armazenamento e preparação de ambiente.
  * **Aplicação prática:** Empregada através de comandos de terminal para realizar a sincronização em massa (`aws s3 sync`) do dataset de imagens ginecológicas direto para o ambiente de execução e para exportar de forma segura o modelo final treinado.

## 🎙️ Módulo de Atendimento Clínico (Análise de Áudio e Texto)

* **`openai-whisper`**
  * **Onde é utilizada:** Na camada inicial de processamento e acessibilidade de áudio.
  * **Aplicação prática:** Atua localmente como o motor de Reconhecimento Automático de Fala (ASR). Ela recebe os arquivos de áudio contendo as gravações das consultas e realiza a decodificação da voz em texto transcrito nativo em português.
* **`librosa`**
  * **Onde é utilizada:** Na extração local de biomarcadores acústicos (DSP - Processamento Digital de Sinais).
  * **Aplicação prática:** Analisa matematicamente o áudio bruto sem dependência de APIs em nuvem. É usada para calcular a frequência fundamental (Pitch) — fornecendo insumos sobre o tom emocional —, detectar zonas de silêncio e metrificar pausas ou taxas de hesitação na fala da paciente.
* **`langchain` / `langchain-core` / `langchain-openai`**
  * **Onde é utilizada:** Na orquestração lógica de inteligência generativa.
  * **Aplicação prática:** Constrói a esteira cognitiva utilizando a sintaxe declarativa **LCEL (LangChain Expression Language)**. Conecta as saídas textuais do Whisper aos modelos LLM, aplicando Engenharia de Prompt Defensiva para assegurar que o texto médico cru seja estruturado estritamente sob as regras e divisões internacionais do prontuário **SOAP**.
* **`deep-translator`**
  * **Onde é utilizada:** Na compatibilização e tradução linguística automatizada.
  * **Aplicação prática:** Utilizada para automatizar a tradução rápida de termos biomédicos específicos durante as etapas intermediárias de processamento, evitando que barreiras linguísticas comprometam a assertividade das instruções fornecidas à inteligência artificial.
* **`transformers` & `tiktoken`**
  * **Onde é utilizada:** No monitoramento de fluxos textuais e governança de custos.
  * **Aplicação prática:** O `tiktoken` faz a contagem preditiva exata e o corte preventivo dos tokens gerados pela transcrição do áudio clínico antes de enviá-los ao LLM, garantindo que o texto não ultrapasse a janela máxima de contexto da API e prevenindo erros de estouro de memória.

## 🩸🎙️ Utilidades Globais (Ambos os Módulos)

* **`numpy` & `pandas`**
  * **Onde são utilizadas:** Na manipulação matemática, estruturação de dados e geração de métricas.
  * **Aplicação prática:** O `numpy` manipula de forma veloz matrizes e tensores numéricos (sejam os pixels das imagens no OpenCV ou os arrays de ondas sonoras no Librosa). O `pandas` organiza as tabelas com o histórico das predições, taxas de acerto e logs, gerando as tabelas e dados estatísticos consolidados no relatório técnico.

<picture>
  <img src="https://img.shields.io/badge/-ebebeb?style=for-the-badge&logoColor=black" width="100%" height="10px" alt="Integrantes do Grupo">
</picture>

# 📊 Datasets Utilizados

Os modelos foram submetidos a treinamentos fundamentados em bases de dados científicas de referência internacional:

* **Vídeo — Dataset GynSurg:** [Gynecology Laparoscopic Surgery Dataset](https://ftp.itec.aau.at/datasets/GynSurge/). Base contendo registros cirúrgicos reais anotados por especialistas clínicos da Universidade Médica de Viena e da Universidade Médica de Toronto. Foram utilizados cerca de 2.041 recortes de vídeos curtos (~5,11 GB de dados totais) divididos estritamente em:
  * **Treino (70%):** 684 com sangramento / 745 sem sangramento.
  * **Validação (20%):** 194 com sangramento / 213 sem sangramento.
  * **Teste (10%):** 99 com sangramento / 106 sem sangramento.
* **Áudio — Audio Recording Whisper:** [Disponível via Kaggle](https://www.kaggle.com/datasets/najamahmed97/audio-recording-whisper). Conjunto de dados composto por diálogos médicos e simulações de consultas clínicas padronizadas pelo formato SOAP.

<picture>
  <img src="https://img.shields.io/badge/-ebebeb?style=for-the-badge&logoColor=black" width="100%" height="10px" alt="Integrantes do Grupo">
</picture>

# 📁 Estrutura de Arquivos Principais

```text
├── MOD_Bleeding/
│   ├── MOD_Bleeding_Train_GPU.ipynb  # Notebook para o ajuste fino (fine-tuning) do YOLOv8 via GPU
│   ├── extract_frames.py             # Script de processamento temporal e espacial usando OpenCV
│   ├── bleeding-detection.py         # Script para simulação e inferência em tempo real com lógica de alertas
│   └── best.pt                       # Pesos exportados do modelo de visão ajustado
│
├── MOD_Atendimento_Clinico/
│   └── MOD_Atendimento_Clinico.ipynb # Notebook da pipeline de áudio, Whisper,
│                                       análise vocal e geração do prontuário SOAP
│
└── README.md                         # Documentação de apresentação do repositório

```

## 📒 Relatório técnico

O Relatório Técnico, disponível pelo link abaixo, detalha todo o passo-a-passo para a construção dos módulos:
[https://github.com/marceloklotz/fiap-quarta-fase](https://github.com/marceloklotz/fiap-terceira-fase-ssp-df/blob/main/relatorio-tecnico-quarta-fase.pdf)

<p align="center">
  <picture><img src="https://github.com/marceloklotz/fiap-quarta-fase/blob/main/assets/relatorio.png" alt="Realatório"></picture>
</p>

## 📽️ Vídeo explicativo

O vídeo explicativo sobre a metologia, resultados e código-fonte utilizado foi disponbilizado a partir do seguinte link:

<p align="center">
<picture>
  <img src="https://github.com/marceloklotz/fiap-quarta-fase/blob/main/assets/tela-youtube.png" width="100%" alt="Integrantes do Grupo">
</picture>
</p>
<p align="center"> Acesso ao vídeo: https://www.youtube.com/watch?v=uGLNE_rOOoI </p>
