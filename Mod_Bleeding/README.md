# 🏫👨‍💻 Módulo para Detecção de Sangramentos

Esta pasta do nosso [repositório](https://github.com/marceloklotz/fiap-quarta-fase/) contém a implementação do **Módulo para Detecção de Sangramentos** em tempo real de cirurgias ginecológicas laparoscópicas, desenvolvido como parte do projeto de visão computacional do Tech Challenge (FIAP).

Contexto médico: a laparoscopia é uma cirurgia minimamente invasiva que utiliza pequenas incisões (de 0,5 a 1 cm) no abdômen para inserir uma microcâmera e instrumentos cirúrgicos. Esse tipo de cirurgia é indicado para endometriose (doença inflamatória), infertilidade, miomas e cistos, dor pélvica crônica, gravidez ectópica (abordagem cirúrgica de escolha para resolver a gestação que ocorre fora da cavidade uterina) e histerectomia (remoção do útero de forma menos traumática).

## 📋 Descrição do Modelo
A ferramenta realiza a análise de vídeos cirúrgicos em tempo real para identificar a ocorrência de sangramentos intraoperatórios. O modelo foi treinado utilizando a arquitetura YOLOv8 (versão Nano - yolov8n-cls.pt), otimizado para oferecer o melhor equilíbrio entre velocidade de inferência e capacidade de aprendizado.  

## ⚠️ Aviso importante
Este modelo foi desenvolvido exclusivamente para fins educacionais. A ferramenta não substitui validações médicas, não está apta para embasar decisões clínicas, realizar diagnósticos ou apoiar triagens.

## 📊 Bases de Dados

O modelo utiliza o dataset GynSurg: Gynecology Laparoscopic Surgery Dataset, composto originalmente por 152 vídeos (1920x1080 a 30fps) de cirurgias ginecológicas laparoscópicas, provenientes da Universidade Médica de Viena e da Universidade Médica de Toronto.  Os vídeos destinados ao treino de classficação para detecção de sangramentos é composto por 2.041 vídeos menores (3 segundos cada), totalizando 977 registros com sangramento e 1.064 sem a presença do evento.

Preparação dos dados: Para o treinamento com YOLOv8, foi realizada a extração de frames utilizando a biblioteca OpenCV, a uma taxa de 1 frame por segundo, totalizando 6.696 arquivos JPG utilizados para o treinamento.

**Referências bibliográficas**
* Título: GynSurg: A Comprehensive Gynecology Laparoscopic Surgery Dataset
* Autores: Sahar Nasirihaghighi and Negin Ghamsarian and Leonie Peschek and Matteo Munari and  Heinrich Husslein and Raphael Sznitman and Klaus Schoeffmann
* Ano: 2025
* Fonte: https://ftp.itec.aau.at/datasets/GynSurge/
* Licença: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (Atribuição-NãoComercial-SemDerivações 4.0 Internacional)

## 🎥 Simulação do Modelo
A simulação em tempo real da detecção de sangramentos foi realizada em ambiente local, utilizando como base a reprodução de um vídeo cirúrgico que não participou do conjunto de treinamento, demonstrando a capacidade do modelo em identificar o evento de forma automatizada. O vídeo foi extraído do repositírio do [World Laparoscopy Training Institute](https://www.laparoscopyhospital.com/laparoscopicvideodownload.html).

## 📒 Relatório técnico

Mais detalhes estão disponíveis no relatório técnico do conjunto de soluções desenvolvidas no escopo deste projeto:
[https://github.com/marceloklotz/fiap-quarta-fase](https://github.com/marceloklotz/fiap-terceira-fase-ssp-df/blob/main/relatorio-tecnico-quarta-fase.pdf)
