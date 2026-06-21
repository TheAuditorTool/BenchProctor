# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import auth_check


async def BenchmarkTest06704(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = base64.b64decode(file_value).decode('utf-8', 'ignore')
    auth_check('user', data)
    return {"updated": True}
