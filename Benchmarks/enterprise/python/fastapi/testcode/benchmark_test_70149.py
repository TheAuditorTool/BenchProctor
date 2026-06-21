# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest70149(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
