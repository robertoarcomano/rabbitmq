from rabbit_mq import Rabbit_MQ
import sys


if len(sys.argv) != 2:
    sys.exit(f"Sintax: {sys.argv[0]} <message>")
rabbit_mq = Rabbit_MQ("hello")
rabbit_mq.send(sys.argv[1])