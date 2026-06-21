# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest73346(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
