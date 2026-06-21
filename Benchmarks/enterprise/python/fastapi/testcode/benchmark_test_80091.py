# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from pydantic import BaseModel
from starlette.responses import JSONResponse
import ast


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest80091(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
