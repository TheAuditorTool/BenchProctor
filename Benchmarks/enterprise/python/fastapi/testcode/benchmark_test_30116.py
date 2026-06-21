# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest30116(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
