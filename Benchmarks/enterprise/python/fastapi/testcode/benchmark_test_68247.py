# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64


async def BenchmarkTest68247(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    eval(str(data))
    return {"updated": True}
