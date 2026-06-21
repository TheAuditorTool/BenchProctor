# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import pickle


async def BenchmarkTest26829(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
