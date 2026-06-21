# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest73667(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
