# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import json
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest17766(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    auth_check('user', data)
    return {"updated": True}
