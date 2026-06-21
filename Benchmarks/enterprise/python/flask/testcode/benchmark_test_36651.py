# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest36651():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    async def _evasion_task():
        return redirect(str(data))
    return asyncio.run(_evasion_task())
