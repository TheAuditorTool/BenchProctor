# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest41223(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<script src="\' + str(data) + \'"></script>\')', '<sink>', 'exec'))
    return _ev['r']
