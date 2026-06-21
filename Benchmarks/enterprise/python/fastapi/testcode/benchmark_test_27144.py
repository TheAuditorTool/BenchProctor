# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json


async def BenchmarkTest27144(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    digest = hashlib.sha256(str(graphql_var).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
