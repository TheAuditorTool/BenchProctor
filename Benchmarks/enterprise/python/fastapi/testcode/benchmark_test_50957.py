# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest50957(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
