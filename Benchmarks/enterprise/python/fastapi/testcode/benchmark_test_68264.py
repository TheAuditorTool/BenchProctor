# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json
from starlette.responses import JSONResponse


async def BenchmarkTest68264(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
