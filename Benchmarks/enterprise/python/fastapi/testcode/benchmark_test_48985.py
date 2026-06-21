# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import json


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest48985(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.chmod('/var/app/data/' + str(processed), 0o777)
    return {"updated": True}
