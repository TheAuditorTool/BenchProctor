# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


def relay_value(value):
    return value

async def BenchmarkTest14488(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    async def _evasion_task():
        return HTMLResponse('<div>' + str(data) + '</div>')
    return await _evasion_task()
