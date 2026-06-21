# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest26997(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    eval(compile("with open('/var/log/app_audit.log', 'a') as fh:\n    fh.write(str(data))", '<sink>', 'exec'))
    return {"updated": True}
