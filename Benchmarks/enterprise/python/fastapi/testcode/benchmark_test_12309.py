# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


def ensure_str(value):
    return str(value)

async def BenchmarkTest12309(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ensure_str(xml_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
