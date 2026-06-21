# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from starlette.responses import HTMLResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest78068(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    def _primary():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
