# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest79706(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
