# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


def normalise_input(value):
    return value.strip()

async def BenchmarkTest29088(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
