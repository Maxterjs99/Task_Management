import main

def completed_task(tasks):
  print("******Tareas Completadas******")
  complete = int(input("Pulse 1 para seleccionar tarea completada. Pulse 2 para eliminar tarea. Pulse 3 para volver a la pestaña principal. =>"))
  if complete == 1:
    task_end(tasks)
  elif complete == 2:
    task_erase(tasks)
  elif complete == 3:
    main.main()
  return tasks

def task_end(tasks):
  print("Lista de tareas:")
  for task in tasks: 
    complete = lambda x : "Si" if x else "No"
    print(f"ID: {task['task_id']}. Tarea: {task['task_name']}. Descripcion: {task['task_description']}. Prioridad: {task['task_pri']}. Completado: {complete(task['task_complete'])}. Hora inicio: {task['task_hour']}:{task['task_minutes']}." )
  
  completed = int(input('seleccione por ID la tarea que completo: '))

  for task in tasks:
    if completed == task['task_id']:
      task['task_complete'] = True
      print('Tarea marcada como completada.')
      return completed_task(tasks)
    
  print('ID no encontrado')
  return completed_task(tasks)

def task_erase(tasks):
  print("Lista de tareas:")
  for task in tasks: 
    complete = lambda x : "Si" if x else "No"
    print(f"ID: {task['task_id']}. Tarea: {task['task_name']}. Descripcion: {task['task_description']}. Prioridad: {task['task_pri']}. Completado: {complete(task['task_complete'])}. Hora inicio: {task['task_hour']}:{task['task_minutes']}." )
  
  erase = int(input('seleccione por ID la tarea que desea eliminar: '))
  
  for task in tasks: 
    if erase == task['task_id']:
      tasks.remove(task)
      print(f'Tarea {erase} borrada.')
      return main.main()
  
  print('ID no encontrado')
  return completed_task(tasks)