# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest28825(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    processed = data[:64]
    exec(str(processed))
    return {"updated": True}
