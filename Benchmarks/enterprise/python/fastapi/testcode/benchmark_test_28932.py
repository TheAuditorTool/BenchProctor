# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import json
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest28932(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
