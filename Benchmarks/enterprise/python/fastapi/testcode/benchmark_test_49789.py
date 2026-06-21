# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest49789(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
