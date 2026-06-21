# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import auth_check


async def BenchmarkTest08313(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    auth_check('user', data)
    return {"updated": True}
