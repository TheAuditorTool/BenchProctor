# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest28527(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
