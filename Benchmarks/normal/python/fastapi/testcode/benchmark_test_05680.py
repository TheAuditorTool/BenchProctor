# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


async def BenchmarkTest05680(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
