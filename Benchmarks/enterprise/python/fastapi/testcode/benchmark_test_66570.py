# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest66570(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
