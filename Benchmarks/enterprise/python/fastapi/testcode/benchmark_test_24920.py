# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest24920(request: Request, field: str = Form('')):
    field_value = field
    allowed = {'config.json', 'index.html', 'readme.md'}
    if field_value not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + field_value
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
