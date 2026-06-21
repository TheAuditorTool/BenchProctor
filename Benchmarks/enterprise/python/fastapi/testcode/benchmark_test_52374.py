# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest52374(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
