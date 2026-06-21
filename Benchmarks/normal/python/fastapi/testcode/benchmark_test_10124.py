# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


async def BenchmarkTest10124(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % (raw_body,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
