# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest53282(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
