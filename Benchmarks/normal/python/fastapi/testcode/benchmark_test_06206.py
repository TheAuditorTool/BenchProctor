# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest06206(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    processed = data[:64]
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
