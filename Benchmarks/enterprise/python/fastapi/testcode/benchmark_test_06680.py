# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from fastapi import Form
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest06680(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
