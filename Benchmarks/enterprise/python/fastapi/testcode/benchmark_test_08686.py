# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def relay_value(value):
    return value

async def BenchmarkTest08686(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = relay_value(upload_name)
    def _primary():
        return HTMLResponse('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
