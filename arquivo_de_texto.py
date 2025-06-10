from cifra_de_blocos import processar_arquivo

# Etapa 1: Criar mensagem em UTF-8 (bytes), salvar em modo binário
mensagem_original = "Informações confidenciais da Inn Seguros.\nCliente: João da Silva"
with open("mensagem.txt", "wb") as f:
    f.write(mensagem_original.encode("utf-8"))

# Etapa 2: Criptografar o arquivo
chave_hex = "1A2B3C4D"
chave = int(chave_hex, 16)
processar_arquivo("mensagem.txt", "mensagem_criptografada.bin", chave, modo="criptografar")

# Etapa 3: Decriptografar
processar_arquivo("mensagem_criptografada.bin", "mensagem_final.txt", chave, modo="decriptografar")

# Etapa 4: Ler e comparar resultado como UTF-8
with open("mensagem_final.txt", "rb") as f:
    mensagem_final = f.read().decode("utf-8", errors="replace")

print("=== MENSAGEM ORIGINAL ===")
print(mensagem_original)
print("\n=== MENSAGEM DECRIPTADA ===")
print(mensagem_final)

if mensagem_original.strip() == mensagem_final.strip():
    print("\n✅ Mensagem decriptada corretamente!")
else:
    print("\n❌ Mensagem decriptada diferente do original.")
