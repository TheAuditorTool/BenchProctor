# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest05717(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    exec(str(data))
    return {"updated": True}
