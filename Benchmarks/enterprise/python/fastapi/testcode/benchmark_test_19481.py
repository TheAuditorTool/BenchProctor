# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest19481(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
