from concurrent.futures import ProcessPoolExecutor
import wmi

# Inicializamos wmi
f = wmi.WMI()

# Presentamos los encabezados para las columnas de los procesos
print("pid    Process name")

# Recorremos todos los proceso en ejecución
for process in f.Win_Process():

    # Mostramos el ID y nombre de los procesos
    print(f"{process.ProcessID:<10} {process.Names}")