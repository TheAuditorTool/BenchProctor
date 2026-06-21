# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest62482(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
