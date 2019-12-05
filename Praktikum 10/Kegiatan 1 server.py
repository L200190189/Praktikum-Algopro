import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50002))
s.listen(5)
print "Program komunikasi tentang data diri"
data = ""
kamus = {"nama" : "Muhammad Habiburrahman",
         "NIM" :"L200190189",
         "angkatan":"2019",
         "keluar":"siap!"}
while data.lower() != "q":
    komm, addr = s.accept()
    while data.lower() != "q":
        data = komm.recv(1024)
        print "Perintah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf perintah anda tidak di mengerti")
                  
