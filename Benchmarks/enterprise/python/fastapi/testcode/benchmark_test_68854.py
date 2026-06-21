# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest68854(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
