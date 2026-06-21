# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest07153(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
