# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest48698(request: Request, req: UserInput):
    json_value = req.payload
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
