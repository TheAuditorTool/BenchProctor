# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest73461(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % str(upload_name)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
