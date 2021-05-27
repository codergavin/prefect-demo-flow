#!/usr/bin/python
# -*- coding: utf-8 -*-
# Company：LineZoneData
# Group: BackEnd
# Author: Gavin
# Motto: Get busy living,or get busy dying!
# Date: 2021/5/26 0026 16:04
# Desc:
from prefect import task, Flow


@task
def create_list():
    return [1, 1, 2, 3]


@task
def add_one(x):
    return x + 1


@task
def get_sum(x):
    return sum(x)


with Flow("simple-map") as f:
    plus_one = add_one.map(create_list)
    plus_two = add_one.map(plus_one)
    result = get_sum(plus_two)

f.run()
