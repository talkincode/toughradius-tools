#!/usr/bin/env python
#coding:utf-8
import os

def auto_install():
    os.system("sudo curl -sSL https://get.daocloud.io/docker | sh")
    os.system("sudo curl -L https://get.daocloud.io/docker/compose/releases/download"
              "/1.5.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose")
    os.system("sudo service docker start")




