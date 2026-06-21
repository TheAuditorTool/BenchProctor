# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import os


async def BenchmarkTest71343(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
