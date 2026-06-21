# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest48151(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    return HTMLResponse('<script src="' + str(data) + '"></script>')
