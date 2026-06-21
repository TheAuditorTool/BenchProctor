# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
import ctypes


async def BenchmarkTest31716(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
