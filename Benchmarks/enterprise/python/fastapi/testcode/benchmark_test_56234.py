# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from pydantic import BaseModel
import ast


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest56234(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
