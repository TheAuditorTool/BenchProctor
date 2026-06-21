# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest24405(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    request.session['data'] = str(data)
    return {"updated": True}
