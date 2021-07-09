import win32com.client

TASK_STATE = {0: 'Unknown',
              1: 'Disabled',
              2: 'Queued',
              3: 'Ready',
              4: 'Running'}

scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()

folders = [scheduler.GetFolder('\\')]
while folders:
    folder = folders.pop(0)
    folders += list(folder.GetFolders(0))
    for task in folder.GetTasks(0):
        if TASK_STATE[task.State] == "Disabled":    # Change for the value you want to remove
            pass
        else:
            print('Path       : %s' % task.Path)
            print('State      : %s' % TASK_STATE[task.State])
            print('Last Run   : %s' % task.LastRunTime)
            print('Last Result: %s\n' % task.LastTaskResult)