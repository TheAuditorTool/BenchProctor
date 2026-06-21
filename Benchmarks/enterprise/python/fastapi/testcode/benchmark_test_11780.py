# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest11780(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return {"updated": True}
