# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel
import json
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest53855(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
