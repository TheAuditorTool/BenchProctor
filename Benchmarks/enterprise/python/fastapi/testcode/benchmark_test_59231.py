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

async def BenchmarkTest59231(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    logging.info('User action: ' + str(data))
    return {"updated": True}
