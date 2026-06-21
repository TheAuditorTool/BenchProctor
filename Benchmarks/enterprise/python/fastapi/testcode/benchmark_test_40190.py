# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest40190(request: Request):
    upload_name = (await request.form()).get('upload', '')
    reader = make_reader(upload_name)
    data = reader()
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
