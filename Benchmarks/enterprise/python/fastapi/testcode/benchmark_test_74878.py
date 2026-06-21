# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


async def BenchmarkTest74878(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
