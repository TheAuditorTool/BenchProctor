# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest34276(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = file_value.decode('utf-8', 'ignore') if isinstance(file_value, bytes) else file_value
    auth_check('user', data)
    return {"updated": True}
