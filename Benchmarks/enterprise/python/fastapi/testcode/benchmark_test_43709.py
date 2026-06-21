# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest43709(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    return HTMLResponse('<img src="' + str(data) + '">')
