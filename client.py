# echo-client
import socket
import sys
server_ip = "192.168.1.147"
server_port = 5566
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
num1 = int(input('輸入數字(請勿超過100):'))
if num1 >= 100:
    print('數字大於等於100，無法顯示')
    sys.exit()
a = "Client of Hegel :"+str(num1)
client.send(a.encode())
print(a)
num2 = client.recv(1024)
num2 = num2.decode('utf8')
print(num2)
num2 = num2.split()
num2 = num2[-1]
sum = int(num1)+int(num2)
if sum < 100:
    print("加總為:"+str(sum))
else:
    print("數字大於等於100，無法顯示")
    sys.exit()
client.close()
