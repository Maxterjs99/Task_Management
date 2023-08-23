import main
import complete_task

"""
Este módulo contiene funciones para gestionar tareas.
"""


def show_tasks(tasks):
  print('******Bienvenido al mostrador de tareas******')
  show = int(input('Pulse 1 para mostrar tareas. Pulse 2 para mostrar solo los nombres de las tareas. Pulse 3 para ordenar por prioridad. Pulse 4 para ir a la ventana de tareas completadas. Pulse 5 para volver a la pestaña principal =>'))
  if show == 1:
    show_all(tasks)
  elif show == 2:
    show_name(tasks)
  elif show == 3:
    show_prio(tasks)
  elif show == 4:
    complete_task.completed_task(tasks)
  elif show == 5:
    main.main()

def show_all(tasks):
  print("******Lista de tareas:")
  for task in tasks: 
    complete = lambda x : "Si" if x else "No"
    print(f"ID: {task['task_id']}. Tarea: {task['task_name']}. Descripcion: {task['task_description']}. Prioridad: {task['task_pri']}. Completado: {complete(task['task_complete'])}. Hora inicio: {task['task_hour']}:{task['task_minutes']}." )
  return show_tasks(tasks)

def show_name(tasks):
  print("******Lista de tareas por nombre:")
  for task in tasks: 
    print(f"Tarea: {task['task_name']}")
  return show_tasks(tasks)

def show_prio(tasks):
  priority= sorted(tasks, key=lambda x: x["task_pri"], reverse=True)
  print("Lista de prioridades y tareas:")
  for task in priority: 
    print(f"Tarea: {task['task_name']}, Prioridad: {task['task_pri']}")
  return show_tasks(tasks)