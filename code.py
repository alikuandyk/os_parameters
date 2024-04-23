import os
import platform
import psutil
import getpass
import socket
import time

def get_os_parameters():
    try:
        os_name = platform.system()  # Название операционной системы
        os_version = platform.version()  # Версия операционной системы
        cpu_info = platform.processor()  # Информация о процессоре

        memory_info = psutil.virtual_memory().total / (1024 ** 3)  # Объем памяти в ГБ
        disk_info = psutil.disk_usage('/').free / (1024 ** 3)  # Доступное дисковое пространство в ГБ

        current_user = getpass.getuser()  # Текущий пользователь

        ip_address = socket.gethostbyname(socket.gethostname())  # IP-адрес
        uptime = round(time.time() - psutil.boot_time(), 2)  # Время безотказной работы системы в секундах
        cpu_usage = psutil.cpu_percent(interval=1)  # Загрузка процессора
        running_processes = [{'PID': p.pid, 'Name': p.name(), 'Memory Usage': p.memory_info().rss / (1024 ** 2)} for p in psutil.process_iter()]  # Запущенные процессы
        disk_partitions = psutil.disk_partitions()  # Разделы диска
        system_architecture = platform.architecture()[0]  # Архитектура системы
        environment_variables = dict(os.environ)  # Переменные среды

        return {
            "OS Name": os_name,
            "OS Version": os_version,
            "CPU Info": cpu_info,
            "Memory (GB)": round(memory_info, 2),
            "Available Disk Space (GB)": round(disk_info, 2),
            "Current User": current_user,
            "IP Address": ip_address,
            "System Uptime (s)": uptime,
            "CPU Usage (%)": cpu_usage,
            "Running Processes": running_processes,
            "Disk Partitions": disk_partitions,
            "System Architecture": system_architecture,
            "Environment Variables": environment_variables
        }
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    os_parameters = get_os_parameters()
    if os_parameters:
        for parameter, value in os_parameters.items():
            print(f"{parameter}: {value}")
