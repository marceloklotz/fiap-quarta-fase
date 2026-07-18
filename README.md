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

-----------------------

# 👩‍⚕️ Inteligência Artificial Multimodal na Saúde da Mulher: Visão Computacional e Análise de Áudio

[![FIAP Postech em IA para Devs](https://img.shields.io/badge/FIAP-Postech%20IA%20para%20Devs-blue?style=for-the-badge)](https://www.fiap.com.br/)
![Fase 4 - Tech Challenge](https://img.shields.io/badge/Fase_4-Tech_Challenge-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![YOLOv8](https://img.shields.io/badge/Ultralytics-YOLOv8-orange?style=flat-square)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-brightgreen?style=flat-square)

Este repositório contém o código-fonte e as especificações técnicas desenvolvidos para o **Tech Challenge da Fase 4** da Pós-Graduação em **Inteligência Artificial para DEVs** da **FIAP (Turma 8IADT)**. O projeto propõe um ecossistema multimodal focado no suporte e na segurança da saúde da mulher, dividido em dois módulos principais: análise preditiva de vídeo intraoperatório e automação de prontuários via inteligência vocal e generativa.

---

## ⚠️ Aviso de Uso Acadêmico e Isenção de Responsabilidade

> **IMPORTANTE:** Os componentes deste repositório foram desenvolvidos exclusivamente para fins educacionais, científicos e de demonstração de viabilidade tecnológica. 
> * **Não substituem validações médicas oficiais.**
> * **Não estão aptos para embasar decisões clínicas em tempo real, realizar diagnósticos ou apoiar triagens hospitalares.**
> * Toda e qualquer interpretação ou uso derivado deste código deve ficar estritamente sob a supervisão de profissionais de saúde competentes.

---

## 🚀 Componentes Principais

O sistema combina capacidades multimodais de **Visão Computacional** e **Processamento de Sinais de Áudio** estruturando-se em dois módulos funcionais:

### 1. 🩸 Módulo Detecção de Sangramentos (Análise de Vídeo)
Desenvolvido para atuar no contexto macro de cirurgias ginecológicas por laparoscopia (cirurgias minimamente invasivas voltadas ao tratamento de endometriose, miomas, cistos ou gravidez ectópica).
* **Objetivo:** Monitorar o fluxo de vídeo e classificar em tempo real a ocorrência de anomalias cirúrgicas como o sangramento intraoperatório.
* **Abordagem Técnico-Científica:** Uma pipeline construída sobre o **YOLOv8** (modelo `yolov8n-cls.pt` ajustado por *fine-tuning*), que analisa os frames processados temporalmente via OpenCV. 
* **Lógica Antibumping / Flickering:** Implementação de uma mecânica de janela deslizante (*sliding window*). O sistema exige a predição consistente acima do limiar de confiança em $X$ frames consecutivos para disparar alertas visuais em formato de moldura vermelha, mitigando alarmes falsos para o cirurgião.

### 2. 🎙️ Módulo Atendimento Clínico (Análise de Áudio)
Uma solução *end-to-end* projetada para apoiar consultas de ginecologia ou obstetrícia a partir do áudio capturado na relação médico-paciente.
* **Processamento Digital de Sinais (DSP):** Extração local de biomarcadores acústicos (tom de voz e taxas de hesitação) sem dependência de nuvem, preservando a latência e a privacidade de dados sensíveis da paciente.
* **Transcrição Automatizada (ASR):** Emprego do modelo **OpenAI Whisper** de forma nativa para transcrição de áudio clínico de forma robusta e resistente a ruídos hospitalares de fundo.
* **Estruturação Cognitiva (LLM):** Integração via sintaxe declarativa **LCEL (LangChain Expression Language)** com Engenharia de Prompt Defensiva para traduzir, contextualizar termos técnicos e gerar automaticamente um prontuário médico estruturado no padrão internacional **SOAP** (Subjetivo, Objetivo, Avaliação e Plano).

---

## 📊 Datasets Utilizados

Os modelos foram submetidos a treinamentos fundamentados em bases de dados científicas de referência internacional:

* **Vídeo — Dataset GynSurg:** [Gynecology Laparoscopic Surgery Dataset](https://ftp.itec.aau.at/datasets/GynSurge/). Base contendo registros cirúrgicos reais anotados por especialistas clínicos da Universidade Médica de Viena e da Universidade Médica de Toronto. Foram utilizados cerca de 2.041 recortes de vídeo curtos (~5,11 GB de dados totais) divididos estritamente em:
  * **Treino (70%):** 684 com sangramento / 745 sem sangramento.
  * **Validação (20%):** 194 com sangramento / 213 sem sangramento.
  * **Teste (10%):** 99 com sangramento / 106 sem sangramento.
* **Áudio — Audio Recording Whisper:** [Disponível via Kaggle](https://www.kaggle.com/datasets/najamahmed97/audio-recording-whisper). Conjunto de dados composto por diálogos médicos e simulações de consultas clínicas padronizadas pelo formato SOAP.

---

## 🛠️ Tecnologias, Bibliotecas e Serviços

O projeto foi construído utilizando o ecossistema Python 3.12 e integra os seguintes componentes:

* **
├── MOD_Atendimento_Clinico/
│   └── MOD_Atendimento_Clinico.ipynb # Notebook da pipeline de áudio, Whisper, análise vocal e geração do prontuário SOAP [cite: 958]
│
└── README.md                         # Documentação de apresentação do repositório
