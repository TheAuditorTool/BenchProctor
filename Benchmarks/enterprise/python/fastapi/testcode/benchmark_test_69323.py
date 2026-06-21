# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest69323(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
