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
