# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest22557(request: Request, req: UserInput):
    json_value = req.payload
    db.execute('DELETE FROM accounts WHERE id = ?', (str(json_value),))
    return {"updated": True}
