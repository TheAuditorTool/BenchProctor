# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest29505(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
