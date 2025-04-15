#!/usr/bin/env python3
import socket
import struct

def compute_checksum(data: bytes) -> int:
    """
    Calcula a soma de verificação (checksum) para um dado pacote de dados.
    Segue o mesmo algoritmo do servidor:
      1. Completa para palavra de 16 bits (se necessário).
      2. Soma em complemento de 1.
      3. Retorna o complemento de 1 da soma.
    """
    print(len(data))
    print("Dados a serem enviados (binário):", ' '.join(format(byte, '08b') for byte in data))
    if len(data) % 2:
        data += b'\0'
        
        print("Dados a serem enviados (binário):", ' '.join(format(byte, '08b') for byte in data))
    s = 0
    for i in range(0, len(data), 2):
        w = data[i] << 8 | data[i+1]
        print("data",data[i])
        print(f"data [i] (binário): {format(data[i], '016b')}")
        print(f"data [i+1] (binário): {format(data[i+1], '016b')}")
        
        print(f"w (binário): {format(w, '016b')}")
        s += w
        print(s)
        s = (s & 0xffff) + (s >> 16)
    return ~s & 0xffff

def main():
    host = '127.0.0.1'
    port = 8080

    # Solicita ao usuário a mensagem a ser enviada
    message = input("Digite a mensagem: ")
    data = message.encode()

    # Calcula a soma de verificação dos dados
    checksum = compute_checksum(data)
    print(f"Soma de verificação calculada: {hex(checksum)}")

    # Empacota o checksum (2 bytes) seguido do payload
    packet = struct.pack("!H", checksum) + data

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(packet)
        # Aguarda resposta do servidor
        response = s.recv(1024)
        print("Resposta do servidor:", response.decode())

if __name__ == '__main__':
    main()
