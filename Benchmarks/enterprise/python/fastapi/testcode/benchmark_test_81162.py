# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def normalise_input(value):
    return value.strip()

async def BenchmarkTest81162(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
