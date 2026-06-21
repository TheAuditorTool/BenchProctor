# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import ast


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest35348(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
