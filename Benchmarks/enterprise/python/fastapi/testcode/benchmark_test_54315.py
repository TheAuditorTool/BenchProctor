# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest54315(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
