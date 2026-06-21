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

async def BenchmarkTest54687(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
