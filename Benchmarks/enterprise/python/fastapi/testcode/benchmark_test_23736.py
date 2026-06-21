# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import HTMLResponse
import unicodedata


@dataclass
class FormData:
    payload: str

async def BenchmarkTest23736(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
