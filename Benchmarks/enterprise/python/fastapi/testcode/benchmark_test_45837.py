# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import base64


async def BenchmarkTest45837(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    globals()['counter'] = int(data)
    return {"updated": True}
