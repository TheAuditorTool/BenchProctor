# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest29821(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
