# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest49750(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
