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

async def BenchmarkTest49793(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return {"updated": True}
