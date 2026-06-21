# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import subprocess


async def BenchmarkTest53193(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
