# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02761(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
