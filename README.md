# 🏫👨‍💻 Tech Challenge - Pós Tech (8IADT) FIAP - Fase 4: Visão computacional aplicada


Este repositório contém um conjunto de soluções em visão computacional para análise de vídeos, com foco na saúde e segurança da mulher, tendo-se em vista o escopo do desafio (Tech Challenge) apresentado no âmbito da quarta fase da Pós Tech (8IADT), da Faculdade de Informática e Administração Paulista (FIAP), conforme requisitos contidos no [PDF](https://github.com/marceloklotz/fiap-quarta-fase/blob/main/Desafio%20-%20Fase%204%20-%20Tech%20challenge%20Secretaria.pdf) disponível no presente repositório. 

A proposta do desafio foi criar um assistente especializado para processar laudos e exames médicos de uma rede hospitalar, monitorando continuamente as pacientes por meio de dados multimodais (áudio, vídeo e  texto) para identificar sinais precoces de risco específicos da saúde e segurança feminina. Dentre as funcionalidades mínimas exigidas, o grupo escolheu prioritariamente: a análise de vídeos (cirurgias ginecológicas) para identificação padrões anômalos ou sinais de desconforto; e a detectação de anomalias em sinais vitais específicos (pressão arterial em gestantes, batimentos fetais), de forma a possibilitar a equipe especializada em tempo real.

Para tanto, utilizou-se o modelo de arquitetura de modelo de visão computacional desenvolvido pela Ultralytics conhecido como [YOLOv8](https://yolov8.com/), apoiado por serviços cognitivos gerenciados em nuvem por meio do Azure Cognitive Services.





## 📝 Descrição do Desafio

A proposta do desafio foi desenvolver um assistente virtual médico personalizado, treinado com dados próprios da instituição, capaz de apoiar condutas clínicas, responder dúvidas de profissionais e sugerir procedimentos alinhados aos protocolos internos de atendimento feminino. O desafio também envolve a criação de fluxos automatizados, seguros e integrados, utilizando LangChain, para coordenar ações como verificação de exames ginecológicos pendentes, recomendação de tratamentos reprodutivos, emissão de alertas para possíveis casos de violência doméstica e articulação de atendimento multidisciplinar, considerando as particularidades e sensibilidades do cuidado à mulher.

Para tanto, utilizou-se o fine-tuning de LLMs com dados específicos da área e implementando fluxos automatizados de decisão clínica através do LangChain, sempre respeitando protocolos de segurança, privacidade e sensibilidade cultural específicos do atendimento feminino, conforme instruções da disciplina da Pós Tech (8IADT) FIAP [(PDF)](https://github.com/marceloklotz/fiap-terceira-fase-ssp-df/blob/main/Desafio-8IADT-Fase3-TechChallenge-Secretaria.pdf).

## 👥 Integrantes do grupo
Os membros do grupo são compostos pelos seguintes servidores da Secretaria de Segurança Pública do Distrito Federal (SSP/DF):

- Alexandre Natã Vicente (**rm370024**) (ale.n.vicente@gmail.com)
- Antônio Cláudio Almeida (**rm370052**) (antonioalmeida@gmail.com)
- Cyd Ferreira Rodrigues (**rm370004**) (cydnelson@gmail.com)
- David Catherink (**rm369997**) (d.catherinck@gmail.com)
- Marcelo Macedo Klotz (**rm370010**) (marceloklotz@gmail.com)

## 🎲 Base de dados

Foi utilizado um dataset sintético (PubMedQA) servindo a dois propósitos complementares: (1) garantir cobertura de temas clinicamente críticos em português (o PubMedQA é majoritariamente em inglês); e (2) fornecer dados de treinamento baseados nas diretrizes brasileiras (FEBRASGO, INCA, Ministério da Saúde) que são as referências aplicáveis no contexto hospitalar nacional. Isso porque dados reais de pacientes são protegidos pela LGPD (Lei Geral de Proteção de Dados) e por normas do CFM (Conselho Federal de Medicina). Em um protótipo acadêmico é inviável usar prontuários reais. Dados sintéticos — gerados manualmente por especialistas ou com auxílio de IA, mas revisados — permitem desenvolver e testar pipelines sem expor informações sensíveis. Esta é prática padrão em pesquisa de IA em saúde.

O PubMedQA é um benchmark biomédico amplamente reconhecido na comunidade científica. Ele contém 1.000 perguntas clínicas extraídas de artigos publicados no PubMed (base de dados de literatura médica da Biblioteca Nacional de Medicina dos EUA).

O desafio exige que o fine-tuning seja realizado com 'dados específicos da área', e o PubMedQA fornece literatura biomédica revisada por pares, com fonte citável (PMID) — atendendo ao critério de “explainability”. Aproximadamente 27% dos registros cobrem temas de saúde feminina diretamente relevantes (ginecologia, obstetrícia, contracepção, câncer de mama, violência, saúde mental materna). O download é feito diretamente do GitHub oficial do projeto, sem necessidade de Google Drive.

O relatório técnico detalha como o código seleciona os registros para aplicar filtros relevantes, resultando em um subconjunto de registros biomédicos com alta relevância para o domínio do trabalho, que foram então convertidos para o formato interno do projeto. Além disso, trata do mapeamento das categorias e dos registros criados manualmente em português, baseados em diretrizes brasileiras e internacionais.
  
## 📒 Relatório técnico

O Relatório Técnico detalha a fundamentação teórica e a implementação prática do assistente, descrevendo uma arquitetura modular em cinco etapas: pré-processamento com anonimização (LGPD), fine-tuning com LoRA, recuperação de informações (RAG/FAISS), orquestração com LangChain e a criação de quatro fluxos clínicos via LangGraph.

O documento aprofunda a estratégia de dados híbrida, combinando literatura biomédica do PubMedQA com diretrizes brasileiras (FEBRASGO, INCA, OMS) em dados sintéticos, além de apresentar uma avaliação quantitativa abrangente por meio de métricas ROUGE, cobertura de termos médicos e uma rigorosa análise de bias e equidade demográfica. Por fim, o relatório discute as considerações éticas, a interpretabilidade das respostas (explainability) e os limites de atuação do protótipo como ferramenta de apoio à decisão.

O download do relatório pode ser feito diretamente pelo seguinte link: 
[https://github.com/marceloklotz/fiap-terceira-fase-ssp-df](https://github.com/marceloklotz/fiap-terceira-fase-ssp-df/blob/main/relatorio-tecnico-terceira-fase.pdf)

## 📽️ Vídeo explicativo

O vídeo explicativo sobre a metologia, resultados e notebook em execução foi disponbilizado a partir do seguinte link:


<p align="center">
  <img src="https://i.ytimg.com/vi/F-G5JFNiwdE/hqdefault.jpg" alt="FIAP - TECH CHALENGE (TERCEIRA FASE)">
</p>
<p align="center"> https://youtu.be/F-G5JFNiwdE </p>
