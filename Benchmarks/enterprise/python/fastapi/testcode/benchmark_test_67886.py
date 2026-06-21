# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest67886(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
