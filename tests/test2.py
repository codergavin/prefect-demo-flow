#!/usr/bin/python
# -*- coding: utf-8 -*-
# Company：LineZoneData
# Group: BackEnd
# Author: Gavin
# Motto: Get busy living,or get busy dying!
# Date: 2021/5/27 0027 10:48
# Desc:

from prefect import task, Flow, Task


@task
def say_hello():
    print("Hello,world!")


@task
def add(x, y=1):
    return x + y


@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))


with Flow("simple-map") as f:
    # result = say_hello("test1111")
    first_result = add(1, y=2)
    print("test111111111111:" + str(first_result))
    second_result = add(x=first_result, y=100)
    print("test111111111111:" + str(second_result))
# f.run()

state = f.run()
print("----------------------")
assert state.is_successful()

first_task_state = state.result[first_result]
assert first_task_state.is_successful()
assert first_task_state.result == 3

second_task_state = state.result[second_result]
assert second_task_state.is_successful()
assert second_task_state.result == 103


class AddTask(Task):

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, x: int, y: int = None) -> int:
        if y is None:
            y = self.default
        return x + y


# # initialize the task instance
# add = AddTask(default=1)


