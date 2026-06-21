# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import re
from starlette.responses import JSONResponse
import json


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest26327(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
