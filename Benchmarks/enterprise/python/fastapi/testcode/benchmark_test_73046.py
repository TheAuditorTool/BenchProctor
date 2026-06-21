# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


async def BenchmarkTest73046(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
