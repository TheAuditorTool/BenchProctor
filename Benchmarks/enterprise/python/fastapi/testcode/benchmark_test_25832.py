# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest25832(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
