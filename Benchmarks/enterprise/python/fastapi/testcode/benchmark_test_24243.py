# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest24243(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = upload_name
    logging.info('User action: ' + str(processed))
    return {"updated": True}
