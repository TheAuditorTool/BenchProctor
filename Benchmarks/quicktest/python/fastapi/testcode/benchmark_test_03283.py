# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import requests


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03283(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
