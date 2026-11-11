# GovIA - Assistente Inteligente de Serviços Públicos

Protótipo desenvolvido para o Programa Futures da Softplan.

## Objetivo

Utilizar Inteligência Artificial para facilitar a
identificação de serviços públicos e direcionar
cidadãos a fontes de informação.

## Tecnologias

- Python
- Streamlit
- Ollama
- Qwen 2.5 (1.5B)

## Funcionalidades

- Interface para perguntas dos usuários.
- Classificação de perguntas com IA local.
- Identificação de solicitações relacionadas à
  certidão de nascimento.
- Indicação de fonte para consulta.
- Tratamento de perguntas fora do escopo.

## Como executar

1. Instale Python e Ollama.
2. Instale as dependências:
   py -m pip install -r requirements.txt
3. Baixe o modelo:
   ollama pull qwen2.5:1.5b
4. Execute:
   py -m streamlit run app.py

## Limitações

O protótipo não fornece procedimentos detalhados
que ainda não tenham sido verificados.

## Fonte de referência

https://www.registrocivil.org.br/
