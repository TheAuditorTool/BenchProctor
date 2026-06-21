# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21353(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    return JSONResponse({'error': str(xml_value), 'stack': repr(locals())}, status_code=500)
