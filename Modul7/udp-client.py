from socket import *  # import semua fungsi dari library socket
import sys  # import modul sys (digunakan untuk operasi sistem, meskipun di sini tidak terlalu digunakan)

# Konfigurasi alamat IP dan port server
serverName = '172.20.10.13'
serverPort = 12000

# Membuat socket UDP
# AF_INET = menggunakan IPv4
# SOCK_DGRAM = menggunakan protokol UDP (connectionless)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Mengatur batas waktu tunggu respon dari server selama 5 detik
clientSocket.settimeout(5)

# Menampilkan instruksi ke user
print("Ketik 'exit' untuk mematikan server dan keluar, atau 'keluar' untuk tutup client saja.\n")

try:
    while True:
        # menerima input dari user
        message = input('Masukkan kalimat lowercase : ')
        
        # validasi jika input kosong, maka ulangi input
        if not message:
            continue

        # mengirim pesan ke server
        # encode() untuk mengubah string menjadi byte
        # sendto() digunakan pada UDP karena tidak perlu koneksi
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # cek apakah user ingin keluar atau mematikan server
        if message.lower() == 'exit':
            print("Perintah exit dikirim. Mematikan server dan menutup klien...")
            break
        elif message.lower() == 'keluar':
            print("Menutup klien...")
            break
        
        try:
            # menerima balasan dari server
            # recvfrom() akan mengembalikan data dan alamat pengirim
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            
            # decode() untuk mengubah byte menjadi string
            print(f"Balasan dari Server: {modifiedMessage.decode()}\n")
        
        except timeout:
            # jika server tidak merespon dalam waktu 5 detik
            print("Kesalahan : Server tidak merespons (Timeout).\n")

# menangani error jika terjadi kesalahan saat program berjalan
except Exception as e:
    print(f"Terjadi kesalahan : {e}")

finally:
    # menutup socket setelah program selesai
    clientSocket.close()
    print("Koneksi ditutup.")