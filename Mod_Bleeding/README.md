# 👩‍⚕️👨‍💻 Inteligência Artificial Multimodal na Saúde da Mulher: Visão Computacional e Análise de Áudio

[![FIAP Postech em IA para Devs](https://img.shields.io/badge/FIAP-Postech%20IA%20para%20Devs-blue?style=for-the-badge)](https://www.fiap.com.br/)
[![Fase 4 - Tech Challenge](https://img.shields.io/badge/Fase_4-Tech_Challenge-purple?style=for-the-badge)](#)
[![Módulo Detecção de Sangramentos](https://img.shields.io/badge/1.Modulo_Detecção_de_Sangramentos-red?style=for-the-badge)](https://github.com/marceloklotz/fiap-quarta-fase/edit/main/Mod_Bleeding/)

## 1. 🩸 Módulo Detecção de Sangramentos (Análise de Vídeo)

Esta pasta do nosso [repositório](https://github.com/marceloklotz/fiap-quarta-fase/) contém a implementação do **Módulo para Detecção de Sangramentos** em tempo real de cirurgias ginecológicas laparoscópicas, desenvolvido como parte do projeto de visão computacional do Tech Challenge (FIAP).

Contexto médico: a laparoscopia é uma cirurgia minimamente invasiva que utiliza pequenas incisões (de 0,5 a 1 cm) no abdômen para inserir uma microcâmera e instrumentos cirúrgicos. Esse tipo de cirurgia é indicado para endometriose (doença inflamatória), infertilidade, miomas e cistos, dor pélvica crônica, gravidez ectópica (abordagem cirúrgica de escolha para resolver a gestação que ocorre fora da cavidade uterina) e histerectomia (remoção do útero de forma menos traumática).

Desenvolvido para atuar no contexto macro de cirurgias ginecológicas por laparoscopia (cirurgias minimamente invasivas voltadas ao tratamento de endometriose, miomas, cistos ou gravidez ectópica).
* **Objetivo:** Monitorar o fluxo de vídeo e classificar em tempo real a ocorrência de anomalias cirúrgicas como o sangramento intraoperatório.
* **Abordagem Técnico-Científica:** Uma pipeline construída sobre o **YOLOv8** (modelo `yolov8n-cls.pt` ajustado por *fine-tuning*), que analisa os frames processados temporalmente via OpenCV. 
* **Lógica Antibumping / Flickering:** Implementação de uma mecânica de janela deslizante (*sliding window*). O sistema exige a predição consistente acima do limiar de confiança em $X$ frames consecutivos para disparar alertas visuais em formato de moldura vermelha, mitigando alarmes falsos para o cirurgião.

## ⚠️ Aviso de Uso Acadêmico e Isenção de Responsabilidade

> **IMPORTANTE:** Os componentes deste repositório foram desenvolvidos exclusivamente para fins educacionais, científicos e de demonstração de viabilidade tecnológica. 
> * **Não substituem validações médicas oficiais.**
> * **Não estão aptos para embasar decisões clínicas em tempo real, realizar diagnósticos ou apoiar triagens hospitalares.**
> * Toda e qualquer interpretação ou uso derivado deste código deve ficar estritamente sob a supervisão de profissionais de saúde competentes.

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

* **`numpy` & `pandas`**
  * **Onde são utilizadas:** Na manipulação matemática, estruturação de dados e geração de métricas.
  * **Aplicação prática:** O `numpy` manipula de forma veloz matrizes e tensores numéricos (sejam os pixels das imagens no OpenCV ou os arrays de ondas sonoras no Librosa). O `pandas` organiza as tabelas com o histórico das predições, taxas de acerto e logs, gerando as tabelas e dados estatísticos consolidados no relatório técnico.
 
# 📊 Dataset Utilizado

O modelo utiliza o dataset GynSurg: [Gynecology Laparoscopic Surgery Dataset](https://ftp.itec.aau.at/datasets/GynSurge/), composto originalmente por 152 vídeos (1920x1080 a 30fps) de cirurgias ginecológicas laparoscópicas, provenientes da Universidade Médica de Viena e da Universidade Médica de Toronto.  Os vídeos destinados ao treino de classficação para detecção de sangramentos é composto por 2.041 vídeos menores (3 segundos cada), totalizando 977 registros com sangramento e 1.064 sem a presença do evento.

Preparação dos dados: Para o treinamento com YOLOv8, foi realizada a extração de frames utilizando a biblioteca OpenCV, a uma taxa de 1 frame por segundo, totalizando 6.696 arquivos JPG utilizados para o treinamento.

**Referências bibliográficas**
* Título: GynSurg: A Comprehensive Gynecology Laparoscopic Surgery Dataset
* Autores: Sahar Nasirihaghighi and Negin Ghamsarian and Leonie Peschek and Matteo Munari and  Heinrich Husslein and Raphael Sznitman and Klaus Schoeffmann
* Ano: 2025
* Fonte: https://ftp.itec.aau.at/datasets/GynSurge/
* Licença: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (Atribuição-NãoComercial-SemDerivações 4.0 Internacional)

## ⚠️ Aviso importante
Este modelo foi desenvolvido exclusivamente para fins educacionais. A ferramenta não substitui validações médicas, não está apta para embasar decisões clínicas, realizar diagnósticos ou apoiar triagens.

## 🎥 Simulação do modelo

A simulação em tempo real da detecção de sangramentos foi realizada em ambiente local, utilizando como base a reprodução de um vídeo cirúrgico que não participou do conjunto de treinamento, demonstrando a capacidade do modelo em identificar o evento de forma automatizada. O vídeo foi extraído do [World Laparoscopy Hospital - WLH](https://www.laparoscopyhospital.com/laparoscopicvideodownload.html).

<p align="center"> Sangramento não detectado </p>
<p align="center">
  <img src="https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/assets/non_bleeding.png?raw=true" alt="Sangramento detectado">
</p>

<p align="center"> Sangramento detectado </p>
<p align="center">
  <img src="https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/assets/bleeding.png?raw=true" alt="Sangramento detectado">
</p>

## 🗂️ Arquivos relacionados

* [MOD_Bleeding_Train_GPU.ipynb](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/MOD_Bleeding_Train_GPU.ipynb) versão final do notebook para treinamento do modelo com uso da T4 GPU do Google Colab.
* [MOD_Bleeding_Train_CPU.ipynb](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/MOD_Bleeding_Train_GPU.ipynb) notebook relacionado ao primeiro modelo treinado a partir da CPU padrão do Google Colab.
* [best.pt](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/best.pt) é o modelo final treinado com o YOLOv8, utilizando o T4 GPU do Google Colab (92,7% de acurácia).
* [best(CPU).pt](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/best.pt) é a versão com o primeiro modelo treinado, utilizando a CPU padrão do Google Colab. (85,3% de acurácia).
* [bleeding-detection.py](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/bleeding-detection.py) é o script para simulação do modelo com detecção em tempo real.
* [extract_frames.py](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Mod_Bleeding/extract_frames.py) é o script utilizado durante a etapa de preparação dos dados (mp4 para jpg).

Os arquivos gerados em JPG (frames extraídos dos vídeos originais) podem ser baixados pelo seguinte link:

* [dataset_yolo.zip](https://drive.google.com/file/d/1SKm4yVZyKHIwbUZf_lAPUS_eWK7bm1bt/view?usp=sharing) (1,4Gb)

O vídeo utilizado (fonte WLH) para simulação em tempo real, também, pode ser encontrado a partir do endereço abaixo (para preservação do repositório):

* [video_cirurgia.mp4](https://drive.google.com/file/d/10V_b3CBWcpIc-EKvvm_m9Uo15Xmxyquu/view?usp=drive_link) (64Mb)

## 📒 Relatório técnico

Mais detalhes estão disponíveis no relatório técnico do conjunto de soluções desenvolvidas no escopo deste projeto:
[https://github.com/marceloklotz/fiap-quarta-fase](https://github.com/marceloklotz/fiap-terceira-fase-ssp-df/blob/main/relatorio-tecnico-quarta-fase.pdf)
