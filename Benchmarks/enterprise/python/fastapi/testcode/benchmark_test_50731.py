# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from fastapi import Form


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest50731(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    def _primary():
        return RedirectResponse(url=str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
