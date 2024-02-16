# echo-server
import socket
import sys
server_ip = "192.168.1.147"
port = 5566
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((server_ip, port))
serv.listen(0)
print(f"Server of Kevin {server_ip}:{port}")
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        from_client = data.decode('utf8')
        print(f"Server of Kevin:{from_client}")
        num2 = int(input('輸入數字:'))
        if num2 >= 100:
            print('數字大於等於100，無法顯示')
            sys.exit()
        serverstr = from_client+" Server of Kevin: " + str(num2)
        conn.send(serverstr.encode())
    conn.close()
