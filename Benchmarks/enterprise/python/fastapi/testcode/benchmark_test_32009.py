# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest32009(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
