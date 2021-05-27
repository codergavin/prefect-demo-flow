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
def say_hello():
    print("-----Hello, world!")


@task(log_stdout=True)
def say_hello(name):
    print("-----Hello, {}!".format(name))


@task
def add(x, y=1):
    return x + y


@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))


flow = Flow("My imperative flow!")

# define some new tasks
name = Parameter("name")
second_add = add.copy()

# add our tasks to the flow
flow.add_task(add)
flow.add_task(second_add)
flow.add_task(say_hello)

# create non-data dependencies so that `say_hello` waits for `second_add` to finish.
say_hello.set_upstream(second_add, flow=flow)

# create data bindings
add.bind(x=1, y=2, flow=flow)
second_add.bind(x=add, y=100, flow=flow)
say_hello.bind(person=name, flow=flow)


















