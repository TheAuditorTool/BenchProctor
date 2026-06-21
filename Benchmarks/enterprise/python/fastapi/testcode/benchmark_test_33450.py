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

async def BenchmarkTest33450(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = handle(multipart_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
