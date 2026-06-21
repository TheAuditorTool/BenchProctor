# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import pickle


request_state: dict[str, str] = {}

async def BenchmarkTest29791(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
