# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest51609(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
