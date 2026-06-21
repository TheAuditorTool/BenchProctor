# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import requests
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest39970(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = handle(api_value)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
