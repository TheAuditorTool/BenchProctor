# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


async def BenchmarkTest16762(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    sys.path.insert(0, str(graphql_var))
    importlib.import_module('report_renderer')
    return {"updated": True}
