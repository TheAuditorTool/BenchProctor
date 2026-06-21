# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest20086(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = ' '.join(str(file_value).split())
    auth_check('user', data)
    return {"updated": True}
