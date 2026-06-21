# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import time
import ast


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04522(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
