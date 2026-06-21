# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import ast
import pickle


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest35429(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
