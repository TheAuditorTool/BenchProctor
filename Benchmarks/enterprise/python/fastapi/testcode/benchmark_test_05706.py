# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest05706(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
