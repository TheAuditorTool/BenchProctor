# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse
import json


async def BenchmarkTest30005(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(graphql_var)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = graphql_var
    logging.info('User action: ' + str(processed))
    return {"updated": True}
