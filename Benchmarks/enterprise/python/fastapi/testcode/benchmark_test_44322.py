# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest44322(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
