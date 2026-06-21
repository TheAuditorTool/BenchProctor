# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest15455(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    request.session['data'] = str(data)
    return {"updated": True}
