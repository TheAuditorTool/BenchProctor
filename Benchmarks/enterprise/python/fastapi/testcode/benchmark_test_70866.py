# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest70866(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data, _sep, _rest = str(file_value).partition('\x00')
    auth_check('user', data)
    return {"updated": True}
