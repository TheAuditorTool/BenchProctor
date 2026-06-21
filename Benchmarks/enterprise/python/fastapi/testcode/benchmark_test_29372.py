# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import ast
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest29372(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    auth_check('user', data)
    return {"updated": True}
