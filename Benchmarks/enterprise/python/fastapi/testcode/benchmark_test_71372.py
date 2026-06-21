# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


def to_text(value):
    return str(value).strip()

async def BenchmarkTest71372(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    await _evasion_task()
    return {"updated": True}
