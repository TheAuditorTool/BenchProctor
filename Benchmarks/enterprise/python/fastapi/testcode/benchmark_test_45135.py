# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest45135(request: Request, req: UserInput):
    json_value = req.payload
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(json_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(json_value))
    return {"updated": True}
