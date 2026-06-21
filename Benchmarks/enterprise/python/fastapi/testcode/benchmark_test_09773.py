# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import urllib.request


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09773(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
