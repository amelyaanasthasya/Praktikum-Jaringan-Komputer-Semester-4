# mengimpor seluruh fungsi dari modul socket
from socket import *

# mengimpor modul threading untuk menjalankan banyak client secara bersamaan
import threading

# fungsi untuk menangani request dari client
def handle_client(connectionSocket):
    try:
        # menerima pesan request dari browser/client maksimal 1024 byte
        message = connectionSocket.recv(1024).decode()

        # mengambil bagian nama file dari request HTTP
        # contoh request: GET /index.html HTTP/1.1
        message = message[4:15]

        # menampilkan nama file yang diminta client
        print(message)

        # membuka file html yang diminta dan menghapus tanda "/"
        f = open(message[1:])
        
        # membaca isi file html
        outputData = f.read()

        # mengirim header HTTP jika file berhasil ditemukan
        connectionSocket.send(
            "HTTP/1.1 200 OK\r\n\r\n".encode()
        )

        # mengirim isi file html ke browser/client
        connectionSocket.sendall(outputData.encode())

        # menutup koneksi client setelah selesai
        connectionSocket.close()

    except IOError:
        # mengirim header HTTP jika file tidak ditemukan
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        )

        # mengirim pesan error ke browser
        connectionSocket.send(
            "<h1>404 Not Found</h1>".encode()
        )

        # menutup koneksi client
        connectionSocket.close()


# membuat socket server menggunakan IPv4 dan TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# menghubungkan server ke port 6789
serverSocket.bind(('', 6789))

# server dapat menampung antrian maksimal 5 client
serverSocket.listen(5)

# menampilkan status bahwa server sedang berjalan
print("[SYSTEM] server is running....")

# perulangan agar server terus menerima client
while True:

    # menerima koneksi dari client
    connectionSocket, addr = serverSocket.accept()

    # membuat thread baru untuk menangani setiap client
    thread = threading.Thread(
        target=handle_client,
        args=(connectionSocket,)
    )

    # menjalankan thread
    thread.start()