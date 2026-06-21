# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest31139(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
