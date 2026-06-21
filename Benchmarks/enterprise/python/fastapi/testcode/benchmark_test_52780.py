# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest52780(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
