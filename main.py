import psutil
import time
from plyer import notification

# Define alert thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_SPACE_THRESHOLD = 80
NETWORK_USAGE_THRESHOLD = 1000  # Bytes per second


def show_desktop_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Duration of the notification in seconds
    )


def check_cpu_usage():
    cpu_percent = psutil.cpu_percent()
    if cpu_percent > CPU_THRESHOLD:
        show_desktop_notification("High CPU Usage Alert", f"CPU usage is at {cpu_percent}%")


def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    if memory_percent > MEMORY_THRESHOLD:
        show_desktop_notification("High Memory Usage Alert", f"Memory usage is at {memory_percent}%")


def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    if disk_percent > DISK_SPACE_THRESHOLD:
        show_desktop_notification("Low Disk Space Alert", f"Disk space usage is at {disk_percent}%")


def check_network_usage():
    network_counters = psutil.net_io_counters()
    bytes_sent = network_counters.bytes_sent
    bytes_recv = network_counters.bytes_recv

    time.sleep(1)

    network_counters_updated = psutil.net_io_counters()
    bytes_sent_updated = network_counters_updated.bytes_sent
    bytes_recv_updated = network_counters_updated.bytes_recv

    sent_speed = bytes_sent_updated - bytes_sent
    recv_speed = bytes_recv_updated - bytes_recv

    if sent_speed > NETWORK_USAGE_THRESHOLD or recv_speed > NETWORK_USAGE_THRESHOLD:
        show_desktop_notification("High Network Usage Alert",
                                  f"Network usage is high: Sent: {sent_speed} B/s, Received: {recv_speed} B/s")


def main():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_space()
        check_network_usage()
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    main()
