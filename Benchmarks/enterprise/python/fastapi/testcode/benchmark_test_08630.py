# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest08630(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
