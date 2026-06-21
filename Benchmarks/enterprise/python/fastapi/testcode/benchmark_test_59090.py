# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest59090(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = handle(prop_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
