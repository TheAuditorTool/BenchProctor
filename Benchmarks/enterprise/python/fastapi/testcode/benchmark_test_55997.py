# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest55997(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    return HTMLResponse('<script src="' + str(data) + '"></script>')
