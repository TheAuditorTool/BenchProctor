# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest34221(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ensure_str(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
