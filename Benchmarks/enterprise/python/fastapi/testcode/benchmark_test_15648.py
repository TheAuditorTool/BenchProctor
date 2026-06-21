# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest15648(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    return HTMLResponse('<img src="' + str(xml_value) + '">')
