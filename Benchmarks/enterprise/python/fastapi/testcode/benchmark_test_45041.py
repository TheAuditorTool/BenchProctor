# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest45041(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
