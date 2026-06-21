# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import re
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest42066(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return {"updated": True}
