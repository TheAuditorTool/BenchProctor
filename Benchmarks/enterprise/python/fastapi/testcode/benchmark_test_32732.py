# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from starlette.responses import HTMLResponse
import ast


async def BenchmarkTest32732(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    async def _evasion_task():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return await _evasion_task()
