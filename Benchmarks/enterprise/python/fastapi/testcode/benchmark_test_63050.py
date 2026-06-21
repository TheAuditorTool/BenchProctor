# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest63050(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return {"updated": True}
