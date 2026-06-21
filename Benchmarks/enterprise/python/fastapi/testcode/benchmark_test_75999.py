# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import json


async def BenchmarkTest75999(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
