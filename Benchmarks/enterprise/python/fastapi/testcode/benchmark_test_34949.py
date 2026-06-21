# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import subprocess


async def BenchmarkTest34949(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
