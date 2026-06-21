# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest14972(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    processed = data[:64]
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(processed)})
