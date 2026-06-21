# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03342(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
