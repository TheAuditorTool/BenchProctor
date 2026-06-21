# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest51088(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    globals()['counter'] = int(data)
    return {"updated": True}
