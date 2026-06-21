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

async def BenchmarkTest78874(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    logging.info('User action: ' + str(data))
    return {"updated": True}
