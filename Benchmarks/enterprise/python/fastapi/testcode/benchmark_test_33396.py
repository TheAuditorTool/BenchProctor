# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest33396(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = handle(multipart_value)
    auth_check('user', data)
    return {"updated": True}
