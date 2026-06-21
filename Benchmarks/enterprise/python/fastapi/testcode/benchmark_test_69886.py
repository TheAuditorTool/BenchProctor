# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def relay_value(value):
    return value

async def BenchmarkTest69886(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = relay_value(xml_value)
    processed = data[:64]
    return HTMLResponse('<div>' + str(processed) + '</div>')
