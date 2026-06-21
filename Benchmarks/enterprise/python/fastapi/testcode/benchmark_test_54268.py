# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest54268(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    return HTMLResponse('<img src="' + str(data) + '">')
