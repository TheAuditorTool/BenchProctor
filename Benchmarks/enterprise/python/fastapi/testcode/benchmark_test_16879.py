# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


async def BenchmarkTest16879(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    with open('/var/uploads/' + str(graphql_var), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
