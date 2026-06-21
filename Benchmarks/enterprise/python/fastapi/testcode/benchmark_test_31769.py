# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest31769(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
