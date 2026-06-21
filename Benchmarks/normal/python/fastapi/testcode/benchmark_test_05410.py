# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest05410(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
