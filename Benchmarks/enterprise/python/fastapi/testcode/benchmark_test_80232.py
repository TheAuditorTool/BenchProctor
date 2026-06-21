# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest80232(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = normalise_input(raw_body)
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
