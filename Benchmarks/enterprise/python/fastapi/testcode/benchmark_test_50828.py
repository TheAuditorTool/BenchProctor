# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest50828(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
