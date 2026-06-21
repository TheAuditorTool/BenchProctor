# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest52322(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = to_text(multipart_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
