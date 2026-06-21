# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import json


async def BenchmarkTest46251(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
