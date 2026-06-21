# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest05068(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
