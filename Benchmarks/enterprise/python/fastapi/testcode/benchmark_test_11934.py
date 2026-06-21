# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest11934(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
