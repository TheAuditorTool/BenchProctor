# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
import json
import asyncio


async def BenchmarkTest25450(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = await fetch_payload()
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
