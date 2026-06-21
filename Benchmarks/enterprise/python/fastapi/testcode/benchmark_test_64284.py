# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse
import json


async def BenchmarkTest64284(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
