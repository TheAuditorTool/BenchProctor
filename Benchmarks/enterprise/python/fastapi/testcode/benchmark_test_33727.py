# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest33727(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = coalesce_blank(xml_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
