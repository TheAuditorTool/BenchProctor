# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest05006(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
