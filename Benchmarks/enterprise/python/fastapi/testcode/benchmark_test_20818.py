# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest20818(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
