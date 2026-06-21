# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest00405(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = multipart_value
    logging.info('User action: ' + str(processed))
    return {"updated": True}
