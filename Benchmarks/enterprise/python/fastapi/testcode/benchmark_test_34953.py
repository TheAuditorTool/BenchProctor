# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


async def BenchmarkTest34953(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
