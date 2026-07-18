# 🏫👨‍💻 Tech Challenge - Pós Tech (8IADT) FIAP - Fase 4: Visão Computacional Aplicada


Este repositório contém um conjunto de soluções em visão computacional para análise de vídeos, com foco na saúde e segurança da mulher, tendo-se em vista o escopo do desafio (Tech Challenge) apresentado no âmbito da quarta fase da Pós Tech (8IADT), da Faculdade de Informática e Administração Paulista (FIAP), conforme requisitos contidos no [PDF](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Desafio%20-%20Fase%204%20-%20Tech%20challenge%20Secretaria.pdf) disponível no presente repositório. 

Como parte da solução proposta para o Tech Challenge, o projeto foi estruturado nos seguintes módulos: 

🩸🚨👨‍💻 **Módulo de Detecção de Sangramentos:** este componente realiza a análise de vídeos em tempo real para identificar sangramentos, no contexto médico cirúrgico. O modelo de visão computacional foi treinado com a arquitetura YOLOv8, utilizando o dataset GynSurg, de cirurgias ginecológicas por laparoscopia. O desenvolvimento atende ao requisito obrigatório de detecção automatizada de “anomalias”, garantindo precisão técnica e agilidade no suporte à decisão das equipes médicas. 

🛡️👩👨‍💻 **Módulo Guardião (BRIEFING – OPÇÃO 1):** permite análise de voz para detectar  se a mulher está em situação de perigo. Trata-se de um protótipo que poderia ser integrado a dispositivos como o Viva-Flor da Secretaria de Segurança Pública do Distrito Federal (SSP/DF), voltado à vítimas de violência doméstica com Medida Protetiva de Urgência (MPU) em vigor, encaminhadas para assistência pelo Ministério Público (MPDFT). O modelo desenvolvido permitiria a análise da voz por meio do Viva-Flor (que funciona como um celular que fica em posse da assistida), que em caso de perigo por detecção de voz, passaria a enviar um alerta automático às equipes que realizam o monitoramento na SSP/DF, mesmo antes da mulher conseguir pressionar o botão para acionar as equipes policiais.

## 👥 Integrantes do grupo
Os membros do grupo são compostos pelos seguintes servidores da Secretaria de Segurança Pública do Distrito Federal (SSP/DF):

- Alexandre Natã Vicente (**rm370024**) (ale.n.vicente@gmail.com)
- Antônio Cláudio Almeida (**rm370052**) (antonioalmeida@gmail.com)
- Cyd Ferreira Rodrigues (**rm370004**) (cydnelson@gmail.com)
- David Catherink (**rm369997**) (d.catherinck@gmail.com)
- Marcelo Macedo Klotz (**rm370010**) (marceloklotz@gmail.com) 

## 🎲 Funcionalidades e datasets

Cada módulo contém uma pasta contendo os arquivos relacionados (notebooks, scripts, datasets) e um README próprio. Favor, acesse as pastas dos respectivos componentes para informações complementares.

## 📒 Relatório técnico

O Relatório Técnico, disponível pelo link abaixo, detalha todo o passo-a-passo para a construção dos módulos:
[https://github.com/marceloklotz/fiap-quarta-fase](https://github.com/marceloklotz/fiap-terceira-fase-ssp-df/blob/main/relatorio-tecnico-quarta-fase.pdf)

## 📽️ Vídeo explicativo

O vídeo explicativo sobre a metologia, resultados e código-fonte utilizado foi disponbilizado a partir do seguinte link:

<p align="center">
  <img src="https://i.ytimg.com/vi/F-G5JFNiwdE/hqdefault.jpg" alt="FIAP - TECH CHALENGE (QUARTA FASE)">
</p>
<p align="center"> https://youtu.be/F-G5JFNiwdE </p>


# 👩‍⚕️ Inteligência Artificial Multimodal na Saúde da Mulher: Visão Computacional e Análise de Áudio

[![(FIAP) Postech em IA para Devs](https://img.shields.io/badge/FIAP-Postech%20IA%20para%20Devs-blue?style=for-the-badge)](https://www.fiap.com.br/)
![Fase 4 - Tech Challenge](https://img.shields.io/badge/Fase_4-Tech_Challenge-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![YOLOv8](https://img.shields.io/badge/Ultralytics-YOLOv8-orange?style=flat-square)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-brightgreen?style=flat-square)

[cite_start]Este repositório contém o código-fonte e as especificações técnicas desenvolvidos para o **Tech Challenge da Fase 4** da Pós-Graduação em **Inteligência Artificial para DEVs** da **FIAP (Turma 8IADT)**. [cite_start]O projeto propõe um ecossistema multimodal focado no suporte e na segurança da saúde da mulher, dividido em dois módulos principais: análise preditiva de vídeo intraoperatório e automação de prontuários via inteligência vocal e generativa[cite: 945].

---

## ⚠️ Aviso de Uso Acadêmico e Isenção de Responsabilidade

> [cite_start]**IMPORTANTE:** Os componentes deste repositório foram desenvolvidos exclusivamente para fins educacionais, científicos e de demonstração de viabilidade tecnológica[cite: 953]. 
> [cite_start]* **Não substituem validações médicas oficiais.** [cite: 953]
> * **Não estão aptos para embasar decisões clínicas em tempo real, realizar diagnósticos ou apoiar triagens hospitalares.** [cite: 953]
> [cite_start]* Toda e qualquer interpretação ou uso derivado deste código deve ficar estritamente sob a supervisão de profissionais de saúde competentes[cite: 954].

---

## 🚀 Componentes Principais

[cite_start]O sistema combina capacidades multimodais de **Visão Computacional** e **Processamento de Sinais de Áudio** estruturando-se em dois módulos funcionais[cite: 945]:

### 1. 🩸 Módulo Detecção de Sangramentos (Análise de Vídeo)
[cite_start]Desenvolvido para atuar no contexto macro de cirurgias ginecológicas por laparoscopia (cirurgias minimamente invasivas voltadas ao tratamento de endometriose, miomas, cistos ou gravidez ectópica)[cite: 948, 960, 961].
* [cite_start]**Objetivo:** Monitorar o fluxo de vídeo e classificar em tempo real a ocorrência de anomalias cirúrgicas como o sangramento intraoperatório[cite: 948, 950].
* [cite_start]**Abordagem Técnica:** Uma pipeline construída sobre o **YOLOv8** (modelo `yolov8n-cls.pt` ajustado por *fine-tuning*) [cite: 949, 967, 970][cite_start], que analisa os frames processados temporalmente via OpenCV[cite: 970]. 
* **Lógica Antibumping / Flickering:** Implementação de uma mecânica de janela deslizante (*sliding window*). [cite_start]O sistema exige a predição consistente acima do limiar de confiança em $X$ frames consecutivos para disparar alertas visuais em formato de moldura vermelha, mitigando alarmes falsos para o cirurgião[cite: 973, 974, 975].

### 2. 🎙️ Módulo Atendimento Clínico (Análise de Áudio)
[cite_start]Uma solução *end-to-end* projetada para apoiar consultas de ginecologia ou obstetrícia a partir do áudio capturado na relação médico-paciente[cite: 951, 952].
* [cite_start]**Processamento Digital de Sinais (DSP):** Extração local de biomarcadores acústicos (tom de voz e taxas de hesitação) sem dependência de nuvem, preservando a latência e a privacidade de dados sensíveis da paciente[cite: 698].
* [cite_start]**Transcrição Automatizada (ASR):** Emprego do modelo **OpenAI Whisper** de forma nativa para transcrição de áudio clínico de forma robusta e resistente a ruídos hospitalares de fundo[cite: 657, 746].
* [cite_start]**Estruturação Cognitiva (LLM):** Integração via sintaxe declarativa **LCEL (LangChain Expression Language)** [cite: 769] [cite_start]com Engenharia de Prompt Defensiva para traduzir, contextualizar termos técnicos e gerar automaticamente um prontuário médico estruturado no padrão internacional **SOAP** (Subjetivo, Objetivo, Avaliação e Plano)[cite: 615, 769].

---

## 📊 Datasets Utilizados

Os modelos foram submetidos a treinamentos fundamentados em bases de dados científicas de referência internacional:

* [cite_start]**Vídeo — Dataset GynSurg:** [Gynecology Laparoscopic Surgery Dataset](https://ftp.itec.aau.at/datasets/GynSurge/)[cite: 949, 959]. [cite_start]Base contendo registros cirúrgicos reais anotados por especialistas clínicos da Universidade Médica de Viena e da Universidade Médica de Toronto[cite: 962, 964]. [cite_start]Foram utilizados cerca de 2.041 recortes de vídeo curtos (~5,11 GB de dados totais) divididos estritamente em[cite: 966, 981]:
  * [cite_start]**Treino (70%):** 684 com sangramento / 745 sem sangramento[cite: 983].
  * [cite_start]**Validação (20%):** 194 com sangramento / 213 sem sangramento[cite: 983].
  * [cite_start]**Teste (10%):** 99 com sangramento / 106 sem sangramento[cite: 983].
* [cite_start]**Áudio — Audio Recording Whisper:** [Disponível via Kaggle](https://www.kaggle.com/datasets/najamahmed97/audio-recording-whisper)[cite: 959]. [cite_start]Conjunto de dados composto por diálogos médicos e simulações de consultas clínicas padronizadas pelo formato SOAP[cite: 614].

---

## 🛠️ Tecnologias, Bibliotecas e Serviços

[cite_start]O projeto foi construído utilizando o ecossistema Python 3.12 e integra os seguintes componentes[cite: 431, 679]:

* [cite_start]**Core ML & Visão:** `ultralytics` (YOLOv8) [cite: 311, 967][cite_start], `opencv-python` (cv2)[cite: 985].
* [cite_start]**Áudio & DSP:** `openai-whisper` [cite: 679][cite_start], `librosa` (extração de pitch, splits e tom)[cite: 679, 721].
* [cite_start]**Orquestração e LLM:** `langchain` / `langchain-core` (arquitetura LCEL)[cite: 679, 769].
* [cite_start]**Utilidades de Texto:** `deep-translator` (tradução livre por web scraping) [cite: 679, 814][cite_start], `transformers`, `tiktoken`[cite: 679].
* [cite_start]**Infraestrutura em Nuvem (Cloud):** **Amazon S3** (`awscli`), utilizado para o armazenamento seguro e sincronização otimizada (`aws s3 sync`) do dataset de imagens e exportação automatizada do arquivo de pesos finais do modelo treinado (`best.pt`)[cite: 206, 391, 885, 886].

---

## 📁 Estrutura de Arquivos Principais

```text
├── MOD_Bleeding/
│   ├── MOD_Bleeding_Train_GPU.ipynb  # Notebook para o ajuste fino (fine-tuning) do YOLOv8 via GPU [cite: 958]
│   ├── extract_frames.py             # Script de processamento temporal e espacial usando OpenCV [cite: 989]
│   ├── bleeding-detection.py         # Script para simulação e inferência em tempo real com lógica de alertas [cite: 958]
│   └── best.pt                       # Pesos exportados do modelo de visão ajustado [cite: 958]
│
├── MOD_Atendimento_Clinico/
│   └── MOD_Atendimento_Clinico.ipynb # Notebook da pipeline de áudio, Whisper, análise vocal e geração do prontuário SOAP [cite: 958]
│
└── README.md                         # Documentação de apresentação do repositório
