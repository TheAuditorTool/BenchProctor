# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest60799(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
