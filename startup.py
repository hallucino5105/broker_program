#!/usr/bin/env python
# coding: utf-8


import sys
import os
import logging as log
import multiprocessing as mp


def exec_picture_viewer():
    pass


def exec_detector():
    pass


def main():
    processes = [
        mp.Process(target=exec_detector),
        mp.Process(target=exec_picture_viewer),
    ]

    for p in processes:
        p.start()


if __name__ == "__main__":
    log.basicConfig(
        format="[%(asctime)s][%(levelname)s] %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=log.DEBUG)

    main()


