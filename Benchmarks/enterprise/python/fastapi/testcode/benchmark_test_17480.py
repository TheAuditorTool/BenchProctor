# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest17480(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(graphql_var) + ',data\n')
    return {"updated": True}
