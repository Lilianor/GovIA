# 🤖 GovIA — Assistente Inteligente de Serviços Públicos

**Protótipo de Inteligência Artificial desenvolvido para o Programa Futures da Softplan.**

## 🎯 O problema

O acesso a serviços públicos pode ser confuso para muitos cidadãos. Informações sobre documentos, solicitações e procedimentos estão distribuídas em diferentes portais, e nem sempre as pessoas sabem qual serviço procurar.

O desafio que motivou o GovIA foi pensar em uma maneira de tornar essa busca mais simples, acessível e intuitiva.

## 💡 A solução

O GovIA é um protótipo de assistente inteligente que recebe perguntas em linguagem natural e utiliza Inteligência Artificial para identificar o serviço público relacionado.

Nesta primeira versão, o projeto foi desenvolvido com foco em dúvidas sobre a segunda via da certidão de nascimento.

Ao identificar o serviço, o GovIA apresenta uma fonte para consulta. Quando os procedimentos detalhados ainda não foram verificados, o aplicativo informa essa limitação ao usuário.

## 🧠 Por que utilizar Inteligência Artificial?

A proposta é permitir que o cidadão descreva sua necessidade com suas próprias palavras, sem precisar conhecer antecipadamente o nome exato de um serviço.

Diferentemente de uma busca baseada exclusivamente em palavras-chave, um modelo de linguagem pode interpretar diferentes maneiras de formular uma mesma solicitação.

O GovIA utiliza o modelo **Qwen 2.5 (1.5B)**, executado localmente por meio do Ollama, para classificar perguntas relacionadas aos serviços públicos.

## 🛠️ Tecnologias utilizadas

- **Python:** desenvolvimento da lógica da aplicação.
- **Streamlit:** construção da interface web.
- **Ollama:** execução local do modelo de IA.
- **Qwen 2.5 (1.5B):** interpretação e classificação das perguntas.
- **Base de conhecimento em TXT:** organização inicial das informações e referências.

## ⚙️ Como desenvolvi a solução

O desenvolvimento foi organizado em etapas:

1. **Definição do problema:** facilitar a identificação de serviços públicos a partir de perguntas em linguagem natural.
2. **Construção da interface:** criação de uma aplicação simples e interativa com Streamlit.
3. **Integração com IA:** utilização do Ollama e do Qwen 2.5 para interpretar e classificar perguntas.
4. **Delimitação do escopo:** escolha da segunda via da certidão de nascimento como primeiro serviço do protótipo.
5. **Organização das informações:** criação de uma base de conhecimento com referências e informações pendentes de verificação.
6. **Testes e ajustes:** avaliação de perguntas relacionadas e não relacionadas ao serviço, com ajustes na classificação e na apresentação das respostas.

Durante os testes, identifiquei um desafio importante: modelos de linguagem podem gerar informações que parecem corretas, mas que não foram confirmadas.

Por isso, optei por limitar as respostas do protótipo, evitando apresentar procedimentos detalhados sem validação prévia.

Essa decisão busca equilibrar o potencial da IA com a responsabilidade de fornecer informações confiáveis.

## ✅ Funcionalidades implementadas

- Interface web para envio de perguntas.
- Classificação de perguntas com IA local.
- Identificação de solicitações relacionadas à certidão de nascimento.
- Tratamento de perguntas fora do escopo.
- Indicação de fonte para consulta.
- Aviso quando informações detalhadas ainda não foram verificadas.

## 💬 Exemplo de utilização

**Pergunta do usuário:**

"Como faço para solicitar a segunda via da minha certidão de nascimento?"

**Comportamento esperado do GovIA:**

- Identifica o serviço relacionado.
- Apresenta a segunda via da certidão de nascimento.
- Informa que os procedimentos detalhados ainda não foram verificados.
- Direciona o usuário ao Portal do Registro Civil.

## 🚀 Como executar o projeto

### Pré-requisitos

- Python instalado.
- Ollama instalado e em execução.

### Instalação

1. Clone ou baixe este repositório.
2. Abra um terminal na pasta do projeto.
3. Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

4. Baixe o modelo de IA:

```bash
ollama pull qwen2.5:1.5b
```

5. Execute a aplicação:

```bash
py -m streamlit run app.py
```

6. Abra o endereço local exibido pelo Streamlit.

**Observação:** os comandos com `py` são destinados ao Windows. Em outros sistemas, pode ser necessário utilizar `python` ou `python3`.

## ⚠️ Limitações do protótipo

O GovIA é um MVP (Produto Mínimo Viável), desenvolvido para demonstrar a aplicação de Inteligência Artificial na identificação de serviços públicos.

Nesta versão:

- O escopo está limitado à identificação de solicitações relacionadas à certidão de nascimento.
- A classificação pode apresentar erros.
- Os procedimentos detalhados ainda dependem de verificação.
- O aplicativo funciona localmente e exige a instalação do Ollama e do modelo de IA.
- O projeto não realiza solicitações ou emissão de documentos.

## 🔮 Possíveis evoluções

- Ampliação para serviços como CPF, RG e CNH.
- Integração com bases de conhecimento verificadas.
- Melhoria na interpretação de perguntas.
- Inclusão de novos fluxos de atendimento.
- Avaliação sistemática da qualidade das classificações.
- Disponibilização de uma versão online.

## 🔗 Fonte de referência

[Portal do Registro Civil](https://www.registrocivil.org.br/)

## 📌 Sobre o projeto

O GovIA foi desenvolvido como projeto prático para o **Programa Futures da Softplan**, com foco em aprendizado, experimentação e aplicação responsável de Inteligência Artificial para solucionar problemas reais.
