# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest40528(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    return HTMLResponse(Template(data).render())
