# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import ast
import defusedxml.ElementTree


async def BenchmarkTest07440(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
