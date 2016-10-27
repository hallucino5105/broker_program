#!/usr/bin/env python
# coding: utf-8


import sys
import os
import logging as log
import subprocess
import multiprocessing as mp


exec_dir = os.path.dirname(__file__)
log_file = "%s/exec.log" % exec_dir


def process_and_wait(cmd, cwd):
    proc = subprocess.Popen(cmd, cwd=cwd, shell=True)
    proc.wait()


def exec_picture_viewer_app():
    cwd = "%s/exec_broker/web" % exec_dir
    cmd = "./backend/app/app.py"

    process_and_wait(cmd, cwd)


def exec_picture_viewer_web():
    cwd = "%s/exec_broker/web" % exec_dir
    cmd = "grunt"

    process_and_wait(cmd, cwd)


def exec_detector():
    cwd = "%s/exec_broker" % exec_dir
    cmd = "./detector.sh '192.168.77.33' 1883"

    process_and_wait(cmd, cwd)


def main():
    processes = [
        mp.Process(target=exec_detector),
        mp.Process(target=exec_picture_viewer_app),
        mp.Process(target=exec_picture_viewer_web),
    ]

    for p in processes:
        p.start()


if __name__ == "__main__":
    log.basicConfig(
        format="[%(asctime)s][%(levelname)s] %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=log.DEBUG)

    main()


