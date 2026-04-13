# SOCKET = digunakan untuk komunikasi jaringan (penjumlahan, pembagian, dll hanya analogi operasi)
from socket import *  # import semua fungsi dari library socket

# menentukan alamat server (localhost = komputer sendiri)
serverName = "localhost"

# menentukan port yang digunakan server
serverPort = 12000 

# membuat socket client
# AF_INET = menggunakan IPv4
# SOCK_STREAM = menggunakan protokol TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# melakukan koneksi ke server menggunakan alamat dan port
clientSocket.connect((serverName, serverPort))

# menampilkan pesan ke user untuk input
print("[SYSTEM] Masukan Pesan")

# variabel kontrol untuk perulangan
running = True
while running:

    # menerima input dari user
    message = input("> ")

    # mengirim pesan ke server
    # encode() digunakan untuk mengubah string menjadi byte
    clientSocket.send(message.encode())

    # jika user mengetik "exit" maka program berhenti
    # lower() digunakan agar input tidak case sensitive (Exit, EXIT, dll tetap dianggap sama)
    if message.lower() == "exit":
        print("[SYSTEM] keluar dari program")
        running = False
        break

    # menerima balasan dari server (maksimal 2048 byte)
    modifierMessage = clientSocket.recv(2048)

    # menampilkan pesan dari server
    # decode() digunakan untuk mengubah byte menjadi string
    print("[SERVER] pesan : ", modifierMessage.decode())

# menutup koneksi socket setelah selesai
clientSocket.close()

# menampilkan bahwa socket sudah ditutup
print("[SYSTEM] socket ditutup")