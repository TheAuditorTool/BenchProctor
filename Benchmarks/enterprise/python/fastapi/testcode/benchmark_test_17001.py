# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest17001(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
