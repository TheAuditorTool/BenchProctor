# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest20759(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    return HTMLResponse(Template(data).render())
