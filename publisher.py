import etcd3

client_1 = etcd3.client()

while True:
    client_1.put("greeting", input())