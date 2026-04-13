from socket import *  # import semua fungsi dari library socket
import sys  # import modul sys untuk keluar dari program

# Konfigurasi port server
serverPort = 12000

# Membuat socket UDP
# AF_INET = menggunakan IPv4
# SOCK_DGRAM = menggunakan protokol UDP (connectionless)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Menghubungkan socket dengan alamat dan port
# '' artinya menerima dari semua alamat IP
serverSocket.bind(('', serverPort))

# Menampilkan bahwa server siap digunakan
print(f"Server UDP siap menerima pesan pada port {serverPort}")
print("Ketik 'exit' dari sisi klien untuk mematikan server secara remote.\n")

try:
    while True:
        # menerima pesan dari client
        # recvfrom() mengembalikan data dan alamat pengirim
        message, clientAddress = serverSocket.recvfrom(2048)
        
        # decode() untuk mengubah byte menjadi string
        # strip() untuk menghapus spasi berlebih
        original_message = message.decode().strip()
        
        # cek apakah client mengirim perintah "exit"
        if original_message.lower() == 'exit':
            print(f"Mematikan server...")
            break
        
        # mengubah pesan menjadi huruf kapital (uppercase)
        modifiedMessage = original_message.upper()
        
        # menampilkan alamat client dan pesan yang diterima
        print(f"Diterima dari {clientAddress[0]}:{clientAddress[1]}: {original_message}")
        print(f"Mengirim balik : {modifiedMessage}")
        
        # mengirim kembali pesan ke client
        # encode() untuk mengubah string menjadi byte
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        
# menangani error jika terjadi kesalahan
except Exception as e:
    print(f"\nTerjadi kesalahan : {e}")

finally:
    # menampilkan bahwa server berhenti
    print("Server telah berhenti.")
    
    # menutup socket server
    serverSocket.close()
    
    # keluar dari program
    sys.exit(0)