# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest22074(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
