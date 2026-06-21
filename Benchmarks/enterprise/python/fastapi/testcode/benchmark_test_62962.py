# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import subprocess


async def BenchmarkTest62962(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
