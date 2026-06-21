# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest10905(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = ensure_str(file_value)
    auth_check('user', data)
    return {"updated": True}
