# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest00547(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    eval(compile("with open('/var/www/html/exports/report.txt', 'w') as fh:\n    fh.write(str(data))", '<sink>', 'exec'))
    return {"updated": True}
