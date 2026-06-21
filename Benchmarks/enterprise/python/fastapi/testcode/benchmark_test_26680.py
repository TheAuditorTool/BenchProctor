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

async def BenchmarkTest26680(request: Request):
    query_array = request.query_params.get('items', '')
    data = handle(query_array)
    logging.info('User action: ' + str(data))
    return {"updated": True}
