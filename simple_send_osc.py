import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

for x in range (90):
  #sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
  #sender.send_message('/filter',random.random()
  cutoff=random.random()*100
  note=int(round(70+random.random()*10))
  sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
  sender.send_message('/trigger/prophet', [note, cutoff, 1])

  time.sleep(0.5)

