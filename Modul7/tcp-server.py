from socket import *  # import semua fungsi dari library socket

# menentukan port server
serverPort = 12000

# membuat socket server
# AF_INET = menggunakan IPv4
# SOCK_STREAM = menggunakan protokol TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# melakukan binding (mengaitkan server dengan alamat dan port)
# '' artinya menerima koneksi dari semua alamat IP
serverSocket.bind(('', serverPort))

# server mulai mendengarkan koneksi dari client
# angka 1 menunjukkan jumlah maksimum antrian koneksi
serverSocket.listen(1)

# menampilkan bahwa server sudah siap
print("[SYSTEM] server tcp siap digunakan")

# variabel kontrol utama
running = True
while running:

    # menerima koneksi dari client
    # connectionSocket = socket khusus untuk komunikasi dengan client
    # addr = alamat client
    connectionSocket, addr = serverSocket.accept()

    while True:
        # menerima pesan dari client (maksimal 2048 byte)
        # decode() digunakan untuk mengubah byte menjadi string
        message = connectionSocket.recv(2048).decode()

        # jika tidak ada pesan, keluar dari loop
        if not message:
            break

        # cek apakah client mengirim "exit"
        # lower() agar tidak case sensitive
        if message.lower() == "exit":
            print("[SYSTEM] client ingin keluar")
            running = False
            break

        # memodifikasi pesan menjadi huruf besar (uppercase)
        modifierMessage = message.upper()

        # menampilkan pesan yang diterima server
        print("[SERVER] server diterima: ", modifierMessage)

        # mengirim kembali pesan ke client
        # encode() untuk mengubah string menjadi byte
        connectionSocket.send(modifierMessage.encode())

    # menutup koneksi dengan client
    connectionSocket.close()

# menutup socket server setelah selesai
serverSocket.close()