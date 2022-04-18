import etcd3

client_2 = etcd3.client()

events_iterator, cancel = client_2.watch("greeting")
for event in events_iterator:
    print("value = %s " % event.value)