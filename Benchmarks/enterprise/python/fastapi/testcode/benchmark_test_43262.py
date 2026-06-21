# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest43262(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % (raw_body,)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
