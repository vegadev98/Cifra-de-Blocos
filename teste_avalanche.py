from cifra_de_blocos import gerar_subchaves, substituicao, permutacao

def criptografar_debug(bloco, chave):
    subchaves = gerar_subchaves(chave)
    print(f"Texto claro: {hex(bloco)}")
    for i in range(3):
        bloco = substituicao(bloco, subchaves[i])
        print(f"Após substituição {i+1}: {hex(bloco)}")
        bloco = permutacao(bloco)
        print(f"Após permutação {i+1}: {hex(bloco)}")
    print(f"Texto cifrado final: {hex(bloco)}\n")
    return bloco

def testar_avalanche():
    bloco = 0x12345678  # Bloco de entrada fixo
    chave1 = 0x1A2B3C4D
    chave2 = 0x1A2B3C4C  # Difere por 1 bit

    print("=== Teste com CHAVE 1 (0x1A2B3C4D) ===")
    criptografar_debug(bloco, chave1)

    print("=== Teste com CHAVE 2 (0x1A2B3C4C) ===")
    criptografar_debug(bloco, chave2)

testar_avalanche()
