#!/bin/env python3
import os
import sys


class Task:
    def execute(self):
        pull = "docker pull {}".format(self.src)
        self.sh(pull)
        tag = "docker tag {} {}".format(self.src,self.dest)
        self.sh(tag)
        push = "docker push {}".format(self.dest)
        self.sh(push)
    def __init__(self,src,dest):
        self.src = src
        self.dest = dest

    def sh(self,cmd):
        code = os.system(cmd)
        if code != 0:
            os._exit(code)

def read_task(file):
    tasks = []
    fh = open(file)
    for line in fh.readlines():
        # 跳过注释
        if line.startswith('#'):
            continue
        if len(line) == 1:
            continue
        if len(line.split()) != 2:
            continue
        (src,dest) = line.split()
        tasks.append(Task(src,dest))
    return tasks


def execut_task(tasks):
    for task in tasks:
        task.execute()

tasks = read_task("image.txt")
execut_task(tasks)
