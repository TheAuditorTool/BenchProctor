# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest49043(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
