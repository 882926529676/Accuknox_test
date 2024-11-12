import psutil
import logging
from datetime import datetime

CPU_THRESHOLD = 80      
MEMORY_THRESHOLD = 80    
DISK_THRESHOLD = 80      
PROCESS_THRESHOLD = 150  


LOG_FILE = "system_health.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_alert(message):
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}% (Threshold: {MEMORY_THRESHOLD}%)")
    return memory_usage

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"High disk usage detected on root partition: {disk_usage}% (Threshold: {DISK_THRESHOLD}%)")
    return disk_usage

def check_process_count():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_alert(f"High process count detected: {process_count} (Threshold: {PROCESS_THRESHOLD})")
    return process_count

def main():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    process_count = check_process_count()

    print("System Health Check -", datetime.now())
    print(f"CPU Usage: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)")
    print(f"Memory Usage: {memory_usage}% (Threshold: {MEMORY_THRESHOLD}%)")
    print(f"Disk Usage (root): {disk_usage}% (Threshold: {DISK_THRESHOLD}%)")
    print(f"Process Count: {process_count} (Threshold: {PROCESS_THRESHOLD})")

if __name__ == "__main__":
    main()
