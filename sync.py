#!/bin/env python3
import pty
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
        (src,dest) = line.split()
        tasks.append(Task(src,dest))
    return tasks


def execut_task(tasks):
    for task in tasks:
        task.execute()
def read_pass(fd):
    return sys.argv[1].encode()

pty.spawn("/usr/bin/docker login -u hellojukay --password-stdin",read_pass)
tasks = read_task("image.txt")
execut_task(tasks)
