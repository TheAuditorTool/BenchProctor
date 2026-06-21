# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import json


async def BenchmarkTest09390(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
