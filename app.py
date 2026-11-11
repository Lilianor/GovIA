
import streamlit as st
import ollama
from pathlib import Path

# CONFIGURAÇÕES
st.set_page_config(
    page_title="GovIA",
    page_icon="🤖",
    layout="centered"
)

MODELO = "qwen2.5:1.5b"
FONTE = "https://www.registrocivil.org.br/"


# CARREGAR BASE DE CONHECIMENTO
def carregar_base_conhecimento():
    caminho = Path(__file__).parent / "base_conhecimento.txt"

    if caminho.exists():
        return caminho.read_text(encoding="utf-8")

    return None


def responder_com_base(pergunta, base):
    resposta = ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é o GovIA, um assistente de serviços públicos. "
                    "Responda exclusivamente com informações confirmadas "
                    "na base de conhecimento fornecida. "
                    "Não invente documentos, valores, prazos ou procedimentos. "
                    "Se a base não contiver a resposta, informe claramente "
                    "que os detalhes ainda não foram verificados. "
                    "Não trate fontes indicadas como se já tivessem sido consultadas. "
                    "Responda em português, de forma clara e objetiva.\n\n"
                    "BASE DE CONHECIMENTO:\n" + base
                )
            },
            {
                "role": "user",
                "content": pergunta
            }
        ],
        options={"temperature": 0}
    )

    return resposta["message"]["content"]

# IDENTIFICAR ASSUNTO COM IA

def identificar_assunto(pergunta):
    texto = pergunta.lower()

    # Proteção para assuntos fora do escopo
    termos_cnh = [
        "cnh",
        "habilitação",
        "carteira de motorista",
        "dirigir",
        "detran"
    ]

    if any(termo in texto for termo in termos_cnh):
        return "OUTRO"

    # Classificação com inteligência artificial
    resposta = ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você classifica perguntas sobre serviços públicos. "
                    "Responda somente CERTIDAO_NASCIMENTO ou OUTRO. "
                    "CERTIDAO_NASCIMENTO é exclusivamente para "
                    "perguntas sobre certidão ou registro de nascimento. "
                    "Perguntas sobre CNH, habilitação, CPF, RG, "
                    "passaporte e outros serviços devem ser OUTRO. "
                    "Em caso de dúvida, responda OUTRO."
                )
            },
            {
                "role": "user",
                "content": pergunta
            }
        ],
        options={"temperature": 0}
    )

    classificacao = resposta["message"]["content"].strip()

    if classificacao == "CERTIDAO_NASCIMENTO":
        return "CERTIDAO_NASCIMENTO"

    return "OUTRO"


# INTERFACE DO GOVIA
st.title("🤖 GovIA")
st.subheader("Assistente Inteligente de Serviços Públicos")

st.write(
    "Bem-vindo ao GovIA! Uma solução que utiliza "
    "Inteligência Artificial para facilitar o acesso "
    "às informações sobre serviços públicos."
)

st.divider()

pergunta = st.text_input(
    "Como posso ajudar você?",
    placeholder="Digite sua dúvida aqui..."
)

if st.button("Enviar pergunta"):

    if not pergunta.strip():
        st.warning("Por favor, digite uma pergunta.")

    else:
        with st.spinner("GovIA está analisando sua pergunta..."):
            try:
                assunto = identificar_assunto(pergunta)

                st.caption("🤖 Classificação realizada com IA local (Qwen 2.5 via Ollama)")

                if assunto == "CERTIDAO_NASCIMENTO":
                    
                    st.success("Encontrei um serviço relacionado!")

                    st.write(
                        "**Serviço:** Segunda via da "
                        "certidão de nascimento"
                    )

                    base = carregar_base_conhecimento()

                    
                    if base:
                        if "Status: Informações detalhadas ainda não verificadas" in base:
                            st.info(
                                "O GovIA identificou o serviço solicitado. "
                                "Entretanto, os procedimentos detalhados "
                                "ainda não foram verificados em fontes oficiais."
                            )

                            st.write("**Fonte para consulta:**")
                            st.markdown(FONTE)

                        else:
                            st.warning(
                                "A base precisa passar por uma "
                                "validação antes de gerar orientações."
                            )

                    else:
                        st.warning(
                            "A base de conhecimento não foi encontrada."
                        )



                else:
                    st.warning(
                        "Ainda não tenho informações "
                        "verificadas sobre esse serviço público."
                    )

            except Exception:
                st.error(
                    "Não foi possível conectar ao Ollama. "
                    "Verifique se ele está em execução."
                )


st.divider()
st.caption("GovIA | Protótipo para o Programa Futures")

st.divider()

with st.expander("📚 Consultar base de conhecimento"):
    conteudo = carregar_base_conhecimento()

    if conteudo:
        st.text(conteudo)
    else:
        st.warning("Base de conhecimento não encontrada.")
