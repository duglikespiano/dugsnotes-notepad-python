#!/usr/bin/env python3
import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = round(du.free / du.total * 100, 2)
    print(f"Disk: {free}% is free")
    return free > 5


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    free = 100 - usage
    print(f"CPU: {free}% is free")
    return free > 25


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!!!")
