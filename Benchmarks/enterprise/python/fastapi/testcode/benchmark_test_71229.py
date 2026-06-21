# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import ast
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest71229(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
