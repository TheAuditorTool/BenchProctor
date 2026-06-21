# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
from starlette.responses import HTMLResponse


async def BenchmarkTest27422(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
