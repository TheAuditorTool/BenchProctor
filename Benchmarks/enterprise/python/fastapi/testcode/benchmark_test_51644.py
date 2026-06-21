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

async def BenchmarkTest51644(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = handle(config_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
