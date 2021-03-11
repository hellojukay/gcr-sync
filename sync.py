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

fh = open("p.text","w")
fh.write(sys.argv[1])
fh.close()

def read_pass(fh):
    fh = open("p.text","r")
    data = os.read(fh,1024)
    return date
pty.spawn("/usr/bin/docker login -u hellojukay --password-stdin",read_pass)
tasks = read_task("image.txt")
execut_task(tasks)
