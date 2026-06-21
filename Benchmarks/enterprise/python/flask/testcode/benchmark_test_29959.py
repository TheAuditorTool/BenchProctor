# SPDX-License-Identifier: Apache-2.0
import requests
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest29959(path_param):
    path_value = path_param
    data = handle(path_value)
    async def _evasion_task():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return asyncio.run(_evasion_task())
