# cifra_de_blocos.py
# Algoritmo de Cifra de Blocos Simétrica de 32 bits com 3 rodadas
#Desenvolvido por VEGADEV

def int_to_bits(n, size=32):
    return [(n >> i) & 1 for i in range(size)][::-1]

def bits_to_int(bits):
    return sum([bit << (len(bits) - 1 - i) for i, bit in enumerate(bits)])

def gerar_subchaves(chave):
    # Gera 3 subchaves de 32 bits por rotação simples
    subchaves = []
    for i in range(3):
        sub = ((chave << (i + 1)) | (chave >> (32 - (i + 1)))) & 0xFFFFFFFF
        subchaves.append(sub)
    return subchaves

def substituicao(bloco, subchave):
    # Substituição reversível: XOR com a subchave
    return bloco ^ subchave

def permutacao(bloco):
    # Troca de metades (16 bits e 16 bits)
    esquerda = (bloco >> 16) & 0xFFFF
    direita = bloco & 0xFFFF
    return (direita << 16) | esquerda

def criptografar_bloco(bloco, chave):
    subchaves = gerar_subchaves(chave)
    for i in range(3):
        bloco = substituicao(bloco, subchaves[i])
        bloco = permutacao(bloco)
    return bloco

def decriptografar_bloco(bloco, chave):
    subchaves = gerar_subchaves(chave)
    for i in reversed(range(3)):
        bloco = permutacao(bloco)  # mesma permutação (auto-inversa)
        bloco = substituicao(bloco, subchaves[i])  # desfaz XOR
    return bloco


def processar_arquivo(nome_entrada, nome_saida, chave, modo="criptografar"):
    with open(nome_entrada, "rb") as f:
        dados = f.read()

    resultado = bytearray()
    for i in range(0, len(dados), 4):
        bloco_bytes = dados[i:i+4].ljust(4, b'\x00')  # padding
        bloco = int.from_bytes(bloco_bytes, byteorder="big")

        if modo == "criptografar":
            bloco_cifrado = criptografar_bloco(bloco, chave)
        else:
            bloco_cifrado = decriptografar_bloco(bloco, chave)

        resultado += bloco_cifrado.to_bytes(4, byteorder="big")

    if modo == "decriptografar":
        # Retira padding (opcional)
        resultado = resultado.rstrip(b"\x00")

    with open(nome_saida, "wb") as f:
        f.write(resultado)


def menu():
    print("=== Cifra de Blocos de 32 bits ===")
    print("1. Criptografar arquivo")
    print("2. Decriptografar arquivo")
    opcao = input("Escolha a opção (1 ou 2): ")

    nome_entrada = input("Nome do arquivo de entrada: ")
    nome_saida = input("Nome do arquivo de saída: ")
    chave_hex = input("Chave (32 bits em hexadecimal, ex: 1A2B3C4D): ")

    try:
        chave = int(chave_hex, 16) & 0xFFFFFFFF
    except ValueError:
        print("Chave inválida.")
        return

    if opcao == "1":
        processar_arquivo(nome_entrada, nome_saida, chave, "criptografar")
        print("Arquivo criptografado com sucesso!")
    elif opcao == "2":
        processar_arquivo(nome_entrada, nome_saida, chave, "decriptografar")
        print("Arquivo decriptografado com sucesso!")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
