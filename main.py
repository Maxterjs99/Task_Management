import add_task
import list_tasks
import complete_task


def main():
  print('******Bienvenido a Gestion de Tareas******')
  choose = int(input('Ingrese 1 para agregar tarea. 2 para mostrar tareas. 3 para mostrar tareas completadas. 4 para salir del programa=>'))

  if choose == 1:
    add_task.add_t()
  elif choose == 2:
    list_tasks.show_tasks(add_task.tasks)
  elif choose == 3:
    complete_task.completed_task(add_task.tasks)
  elif choose == 4:
    return

if __name__ == "__main__":
  main()