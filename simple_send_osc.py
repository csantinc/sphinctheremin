import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

for x in range (90):
  sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
  sender.send_message('/filter',random.random())
  time.sleep(1)

