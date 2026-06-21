# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02375(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
