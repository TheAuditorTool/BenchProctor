# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest06331(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
