import random
import argparse
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to send to")
  parser.add_argument("--port",
      type=int, default=4559, help="The port to send to")
  args = parser.parse_args()

  for x in range (100):
    sender = udp_client.SimpleUDPClient(args.ip, args.port)
    msg='/filter'
    value=random.random()
    sender.send_message(msg,value)
    print('Sent message: ',msg,' ',value)
    time.sleep(1)

