# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest74788(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JSONResponse({'allocated': allocated}, status_code=200)
