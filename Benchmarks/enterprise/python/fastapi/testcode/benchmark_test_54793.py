# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest54793(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
