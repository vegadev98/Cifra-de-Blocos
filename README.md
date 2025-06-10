# 🔐 Algoritmo de Cifra de Blocos – Inn Seguros

Este projeto implementa uma cifra de blocos **simétrica** de 32 bits com **3 rodadas**, desenvolvida em **Python puro**, sem bibliotecas externas. O algoritmo realiza criptografia e descriptografia de arquivos utilizando:

- 🔁 Substituição (XOR)
- 🔃 Permutação (troca de metades)
- 🔑 Subchaves geradas por rotação da chave principal

---

## 📦 Funcionalidades

- ✅ Criptografia simétrica (mesma chave para cifrar e decifrar)
- 📦 Blocos e chaves de 32 bits
- 🔁 3 rodadas com subchaves derivadas
- 💥 Efeito avalanche comprovado
- 🧾 Suporte a arquivos binários e textos
- 🧩 Sem dependências externas

---

## 🚀 Como usar

### 📋 Requisitos
- Python 3.x

### ▶️ Passo a passo


# 1. Clone o repositório
git clone https://github.com/seu-usuario/cifra-blocos.git
cd cifra-blocos

# 2. Execute o programa
python cifra_de_blocos.py


### 📌 No terminal, escolha:

* `1` para **criptografar**
* `2` para **decriptografar**

### 📝 Informe:

* Arquivo de entrada (ex: `mensagem.txt`)
* Arquivo de saída (ex: `mensagem.cript`)
* Chave de 32 bits em hexadecimal (ex: `1A2B3C4D`)

---

## 🧪 Teste do Efeito Avalanche

Rode o script de teste para observar o comportamento do efeito avalanche:

```bash
python teste_avalanche.py
```

O teste compara os resultados da cifra usando duas chaves que diferem por **1 bit**.

---

## 📁 Estrutura dos Arquivos

| Arquivo                      | Função                                    |
| ---------------------------- | ----------------------------------------- |
| `cifra_de_blocos.py`         | Código principal da cifra                 |
| `teste_avalanche.py`         | Script de verificação do efeito avalanche |
| `mensagem.txt`               | Exemplo de arquivo de entrada             |
| `mensagem_criptografada.bin` | Arquivo cifrado gerado pelo algoritmo     |
| `mensagem_final.txt`         | Resultado da descriptografia              |

---

> Projeto desenvolvido para a disciplina **Segurança de Sistemas e Criptografia**.
