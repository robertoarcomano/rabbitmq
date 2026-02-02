import pika 


class Rabbit_MQ:
    def __init__(self, queue):
        self.queue = queue
        self.server = "localhost"
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.server))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def send(self, body):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=body)
        print("Messagge sent")

    def recv(self):
        def callback(ch, method, properties, body):
            print(f"Message received: {body}")
        self.channel.basic_consume(queue=self.queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":
    rabbit_mq = Rabbit_MQ("hello")
    rabbit_mq.send("ok")
    rabbit_mq.recv()
