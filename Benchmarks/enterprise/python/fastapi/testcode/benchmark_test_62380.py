# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


def relay_value(value):
    return value

async def BenchmarkTest62380(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
