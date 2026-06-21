# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import json
import importlib
import sys


@dataclass
class FormData:
    payload: str

async def BenchmarkTest65869(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
