import time
class Process:
  def __init__(self, name, time_cpu, ticket):
    self.name = name
    self.time_cpu = time_cpu
    self.ticket = ticket
    self.waiting = True
    self.running = False
    self.blocked = False

  def run(self):
    self.waiting = False
    self.running = True
    if self.running and self.time_cpu > 0:
      print("Process "+self.name+" running...")
      self.time_cpu -= 1
    else:
      print("Process "+self.name+" completed.")
      self.running = False
      self.terminated = True

  def __str__(self):
    state = "Process: "+self.name+". Time CPU: "+str(self.time_cpu)+". Ticket: "+str(self.ticket)
    return state

import random

def ticket_randon(number_ticket, list_ticket):
  number = []
  while number_ticket > 0:
    ticket = random.randint(1,len(list_ticket)+1)

    if ticket not in list_ticket:
      list_ticket.append(ticket)
      number.append(ticket)
      number_ticket -= 1

  return number

def del_ticket_process(process_ticket, list_ticket):
    for number in process_ticket:
        list_ticket.remove(number)  

    return list_ticket

def win_process(list_ticket, list_process):
  win_ticket = random.choice(list_ticket)
  print("Winning ticket:" + str(win_ticket))
  for process in list_process:
    if win_ticket in process.ticket:
      win_process_number = list_process.index(process)
      return win_process_number

list_ticket = []
list_process = []
list_process.append(Process("Pintar", 3, ticket_randon(3, list_ticket)))
list_process.append(Process("Secar", 4, ticket_randon(5, list_ticket)))
list_process.append(Process("Pulir", 2, ticket_randon(1, list_ticket)))
list_process.append(Process("Tapizar", 3, ticket_randon(2, list_ticket)))

# Lista de procesos 
# print("lista de ticket: "+ str(list_ticket))
# print("lista de procesos en listo: ")
# for process in list_process:
#   print(process)

# # Selección del proceso ganador

# in_cpu = win_process(list_ticket, list_process)
# print("in_cpu", str(in_cpu))
# list_process[in_cpu].running = True
# print("Winning process: "+ str(in_cpu) +" - " +str(list_process[in_cpu].name))

# # Pasar el proceso a ejecutar
# for process in list_process:
#   if process.running == True:
#     process.run()
#     list_ticket = del_ticket_process(process.ticket, list_ticket)
#     list_process.remove(process)

# # Listo de procesos existentes
# print("lista de procesos en listo: ")
# for process in list_process:
#   print(process)
# print("lista de tickets: "+ str(list_ticket))