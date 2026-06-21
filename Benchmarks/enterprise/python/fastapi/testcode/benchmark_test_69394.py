# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest69394(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    return HTMLResponse('<script src="' + str(data) + '"></script>')
