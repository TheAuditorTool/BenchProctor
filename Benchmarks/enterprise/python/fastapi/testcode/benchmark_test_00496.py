# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest00496(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = relay_value(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
