# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest50174(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    def _primary():
        return RedirectResponse(url=str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
