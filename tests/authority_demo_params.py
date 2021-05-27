#!/usr/bin/python
# -*- coding: utf-8 -*-
# Company：LineZoneData
# Group: BackEnd
# Author: Gavin
# Motto: Get busy living,or get busy dying!
# Date: 2021/5/26 0026 15:42
# Desc: 官方Demo
from prefect import task, Flow, Parameter


@task(log_stdout=True)
def say_hello(name):
    print("-----Hello, {}!".format(name))


with Flow("My First Flow") as flow:
    # 含参数
    name = Parameter('name')
    say_hello(name)


flow.run(name='world')  # "Hello, world!"
flow.run(name='Marvin')  # "Hello, Marvin!"
