# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import json
from starlette.responses import JSONResponse


async def BenchmarkTest53187(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
