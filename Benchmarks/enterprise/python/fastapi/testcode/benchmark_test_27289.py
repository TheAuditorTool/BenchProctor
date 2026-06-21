# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import ast


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest27289(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
