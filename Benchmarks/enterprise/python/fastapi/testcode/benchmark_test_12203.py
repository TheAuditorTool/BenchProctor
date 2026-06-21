# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest12203(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    eval(str(data))
    return {"updated": True}
