# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest12271(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
