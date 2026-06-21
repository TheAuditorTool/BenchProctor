# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import importlib


async def BenchmarkTest17920(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    importlib.import_module(str(data))
    return {"updated": True}
