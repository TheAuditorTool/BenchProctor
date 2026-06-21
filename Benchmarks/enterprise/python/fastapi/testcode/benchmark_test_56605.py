# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import socket


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest56605(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    processed = data[:64]
    s = socket.create_connection((str(processed), 80))
    s.close()
    return {"updated": True}
