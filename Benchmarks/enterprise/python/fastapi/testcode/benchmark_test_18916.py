# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import ast


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest18916(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JSONResponse({'allocated': allocated}, status_code=200)
