# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json
import ast


async def BenchmarkTest29402(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    logging.info('User action: ' + str(data))
    return {"updated": True}
