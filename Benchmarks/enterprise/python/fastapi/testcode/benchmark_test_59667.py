# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import json


async def BenchmarkTest59667(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
