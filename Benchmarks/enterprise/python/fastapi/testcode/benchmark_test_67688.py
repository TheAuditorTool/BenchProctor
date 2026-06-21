# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest67688(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
