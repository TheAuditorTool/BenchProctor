# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest56672(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
