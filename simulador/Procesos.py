import random

class Process:
  def __init__(self, name, burst_time, arrival_time):
    self.name = name
    self.burst_time = burst_time ## tiempo de procesamiento
    self.time_cpu = burst_time  ## tiempo restante de procesamiento
    self.arrival_time = arrival_time  ## tiempo de llegada del proceso
    self.wait_time = 0
    self.block_time = 0 # tiempo en lista de bloqueado
    self.time_blocked = 0 # Tiempo total bloqueado
    self.lock_number = 0
    self.completion_time = 0  # tiempo de finalización
    self.ticket = []
    self.waiting = True
    self.running = False
    self.blocked = False
    self.terminated = False

  def give_ticket(self, ticket):
    self.ticket.extend(ticket)

  def run(self):
    self.running = True
    if self.time_cpu > 1:
      print("Process "+self.name+" running...")
    else:
      print("Process "+self.name+" completed.")
      self.running = False
      self.terminated = True
    return -1
  
  def __str__(self):
    if not(self.blocked):
      state = "Proceso: "+self.name+"\n-T. Procesamiento: "+str(self.time_cpu)+"/"+str(self.burst_time)+"\n-T. Llegada: "+str(self.arrival_time)+"\n-T. Espera: "+str(self.wait_time)+"\n-T.T. Bloquedo: "+str(self.time_blocked)+"/#Blq: "+str(self.lock_number)
      if len(self.ticket) != 0:
        state = state + ("\n-Ticket: "+str(self.ticket))
      if self.terminated:
        state = state + ("\n-T. Finalización: "+str(self.completion_time))
    else:
      state= "Proceso: "+self.name + "\n-T. Bloqueado: "+str(self.block_time)
    return state

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

def win_process(win_ticket, list_process):
  for process in list_process:
    if win_ticket in process.ticket:
      win_process_number = list_process.index(process)
      return win_process_number

