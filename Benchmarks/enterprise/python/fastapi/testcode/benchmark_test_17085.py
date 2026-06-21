# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest17085(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    def _primary():
        return HTMLResponse('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
