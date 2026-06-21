# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest52796(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = to_text(file_value)
    auth_check('user', data)
    return {"updated": True}
