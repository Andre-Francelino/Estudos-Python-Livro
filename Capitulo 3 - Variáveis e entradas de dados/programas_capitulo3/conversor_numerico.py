numero = 28  # Número decimal que queremos converter

# Converter para binário
binario = bin(numero)[2:]  # O [2:] remove o prefixo '0b'
print(f"Binário: {binario}")

# Converter para octal
octal = oct(numero)[2:]  # O [2:] remove o prefixo '0o'
print(f"Octal: {octal}")

# Converter para hexadecimal
hexadecimal = hex(numero)[2:].upper()  # O [2:] remove o prefixo '0x' e upper() deixa em maiúsculo
print(f"Hexadecimal: {hexadecimal}")
