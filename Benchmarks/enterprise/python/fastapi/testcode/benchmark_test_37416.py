# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest37416(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
