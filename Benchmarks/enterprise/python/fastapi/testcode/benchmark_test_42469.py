# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import importlib


async def BenchmarkTest42469(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    importlib.import_module(str(data))
    return {"updated": True}
