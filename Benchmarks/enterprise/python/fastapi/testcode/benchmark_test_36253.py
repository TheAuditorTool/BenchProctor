# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import requests


@dataclass
class FormData:
    payload: str

async def BenchmarkTest36253(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
