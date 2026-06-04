# 🏫👨‍💻 Tech Challenge - Pós Tech (8IADT) FIAP - Fase 4: Visão Computacional Aplicada


Este repositório contém um conjunto de soluções em visão computacional para análise de vídeos, com foco na saúde e segurança da mulher, tendo-se em vista o escopo do desafio (Tech Challenge) apresentado no âmbito da quarta fase da Pós Tech (8IADT), da Faculdade de Informática e Administração Paulista (FIAP), conforme requisitos contidos no [PDF](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Desafio%20-%20Fase%204%20-%20Tech%20challenge%20Secretaria.pdf) disponível no presente repositório. 

A proposta do desafio foi criar um assistente especializado para processar laudos e exames médicos de uma rede hospitalar, monitorando continuamente as pacientes por meio de dados multimodais (áudio, vídeo e  texto) para identificar sinais precoces de risco específicos da saúde e segurança feminina. Dentre as *funcionalidades mínimas* exigidas, o grupo escolheu a seguinte metodologia: 

1. A análise de vídeos para identificação de padrões anômalos ou sinais de desconforto por meio do dataset [GynSyurge](https://ftp.itec.aau.at/datasets/GynSurge/) de cirurgias ginecológicas de laparacospia, vislumbrando a entrega técnica (requisito obrigatório) de  detecção de complicações, sangramento anômalo. O dataset foi publicizado a partir da Cornell University: https://arxiv.org/abs/2506.11356.
2.  A detectação de anomalias em sinais vitais de pressão arterial em gestantes e de batimentos fetais a partir da análise do [CTU-UHB Intrapartum CTG Database (2014)](https://physionet.org/content/ctu-uhb-ctgdb/1.0.0/), da Czech Technical University (CTU) in Prague e da University Hospital in Brno (UHB), de forma a possibilitar o cumprimento dos seguintes **objetivos**: detecção precoce de riscos em saúde materna e ginecológica; e aplicação de técnicas de detecção de anomalias em tempo real para  monitoramento preventivo específico.
3. Uso do modelo de arquitetura de modelo de visão computacional desenvolvido pela Ultralytics conhecido como [YOLOv8](https://yolov8.com/), apoiado por serviços cognitivos gerenciados em nuvem por meio do **Azure Cognitive Services** para integração, resguaradando os padrões de privacidade e segurança para dados sensíveis exigidos.

## 👥 Integrantes do grupo
Os membros do grupo são compostos pelos seguintes servidores da Secretaria de Segurança Pública do Distrito Federal (SSP/DF):

- Alexandre Natã Vicente (**rm370024**) (ale.n.vicente@gmail.com)
- Antônio Cláudio Almeida (**rm370052**) (antonioalmeida@gmail.com)
- Cyd Ferreira Rodrigues (**rm370004**) (cydnelson@gmail.com)
- David Catherink (**rm369997**) (d.catherinck@gmail.com)
- Marcelo Macedo Klotz (**rm370010**) (marceloklotz@gmail.com)

## 🎲 Bases de dados utilizadas

**Gynecology Laparoscopic Surgery**

O GynSurg: Gynecology Laparoscopic Surgery Dataset é um componente de reconhecimento de ações que consiste em 152 vídeos de cirurgias laparoscópicas ginecológicas, selecionados a partir de mais de 600 procedimentos registrados na Universidade Médica de Viena e na Universidade Médica de Toronto, conforme [artigo](Cornell University: https://arxiv.org/abs/2506.11356) publicado na Cornell University. Todos os vídeos foram capturados a 30 quadros por segundo (fps) com uma resolução de 1920x1080 pixels. Cada vídeo foi meticulosamente anotado por especialistas clínicos para quatro ações operatórias fundamentais: coagulação, passagem de agulha, sucção/irrigação e transecção. Adicionalmente, um subconjunto dedicado dos dados foi anotado para dois efeitos colaterais intraoperatórios — sangramento e fumaça — visando apoiar pesquisas sobre o reconhecimento de ações e eventos complexos em cirurgias laparoscópicas.

Contexto: A laparoscopia ginecológica é uma cirurgia minimamente invasiva que utiliza pequenas incisões (de 0,5 a 1 cm) no abdômen para inserir uma microcâmera e instrumentos cirúrgicos. O abdômen é preenchido com gás para dar espaço e visibilidade ao cirurgião. Ela permite ao médico examinar os órgãos internos da pelve e realizar procedimentos com mais precisão, menos dor e recuperação mais rápida que a cirurgia aberta. Suas principais indicações na ginecologia incluem: endometriose (doença inflamatória), infertilidade, miomas e cistos, dor pélvica crônica, gravidez ectópica (abordagem cirúrgica de escolha para resolver a gestação que ocorre fora da cavidade uterina) e histerectomia (remoção do útero de forma menos traumática).

Motivação técnica: o dataset permite a visualização por vídeo, já que a cirurgia laparoscópica é realizada com o auxílio de câmeras que geram vídeos de alta resolução (1920x1080 pixels) do interior do corpo da paciente, a partir de instrumentação especializada: o procedimento utiliza instrumentos específicos que a IA deve ser capaz de detectar, como pinças (graspers), tesouras, agulhas, irrigadores, porta-agulhas e ganchos (hooks). Além disso, durante os procedimentos cirúrgicos são realizadas ações como coagulação, passagem de agulha, sucção/irrigação e transecção (corte), que permitem o cumprimento do desafio proposto para a detecção de anomalias e intercorrências, como sangramentos e mesmo a presença de fumaça. Isso porque a laparoscopia, gases são usados para insuflar a cavidade abdominal, criando um espaço de trabalho seguro para a visualização dos órgãos. A fumaça surge como subproduto do uso de instrumentos cirúrgicos de corte/cautério, sendo a detecção importante para evitar problemas respiratórios pelas equipes e até mesmo a obstrução das imagens das câmeras pelos gases.

Referências bibliográficas
Título: GynSurg: A Comprehensive Gynecology Laparoscopic Surgery Dataset
Autores: Sahar Nasirihaghighi and Negin Ghamsarian and Leonie Peschek and Matteo Munari and  Heinrich Husslein and Raphael Sznitman and Klaus Schoeffmann
Ano: 2025

**CTU-UHB Intrapartum CTG Database (2014)**



## 📒 Relatório técnico

O Relatório Técnico, disponível pelo link abaixo, detalha a fundamentação teórica e a implementação prática:
[https://github.com/marceloklotz/fiap-quarta-fase](https://github.com/marceloklotz/fiap-terceira-fase-ssp-df/blob/main/relatorio-tecnico-quarta-fase.pdf)

## 📽️ Vídeo explicativo

O vídeo explicativo sobre a metologia, resultados e notebook em execução foi disponbilizado a partir do seguinte link:

<p align="center">
  <img src="https://i.ytimg.com/vi/F-G5JFNiwdE/hqdefault.jpg" alt="FIAP - TECH CHALENGE (QUARTA FASE)">
</p>
<p align="center"> https://youtu.be/F-G5JFNiwdE </p>
