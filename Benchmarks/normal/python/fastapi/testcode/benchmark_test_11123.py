# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest11123(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = default_blank(ua_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    exec(str(processed))
    return {"updated": True}
