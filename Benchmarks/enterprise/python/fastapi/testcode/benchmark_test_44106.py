# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import defusedxml.ElementTree


async def BenchmarkTest44106(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
