# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest11949(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    result = 100 / int(str(data))
    return {"updated": True}
