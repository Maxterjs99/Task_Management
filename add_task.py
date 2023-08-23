import list_tasks 
tasks = []

def add_task():
  while True:
    task = {}
    task_id(task, tasks)
    tasks.append(task)
    add_another = input("¿Agregar otra tarea? (s/n): ")
    if add_another.lower() != "s":
      break
  return show_tasks(tasks)
  
def task_id(task, tasks): 
  task['task_id'] = len(tasks) +1
  return task_name(task)

def task_name(task):
  task["task_name"] = str(input('Ingrese nombre de la tarea = '))
  return task_description(task)

def task_description(task):
  task["task_description"] = str(input('Descripcion de la tarea = '))
  return task_priority(task)

def task_priority(task):
  pri_count = True
  while pri_count:
    priority = int(input('Ingrese del 1-10 el nivel de prioridad de la tarea = '))
    if 0 <= priority <= 10:
      task["task_pri"] = int(priority)
      return task_hour(task)
    else:
      print("Entrada de prioridad incorrecta")
      continue

def task_hour(task):
  hour_count = True
  while hour_count:
    user_hour = input("Ingresa la hora de inicio (formato HH:MM): ")
    hour, minutes = map(int, user_hour.split(":"))
    
    if 0 <= hour <= 23 and 0 <= minutes <= 59:
      task["task_hour"] = int(hour)
      task["task_minutes"] = format(int(minutes), ".2g")
      return complete_task(task)
    else:
      print("Entrada de hora incorrecta")
      continue

def complete_task(task): 
  task['task_complete'] = False
  return 
      
