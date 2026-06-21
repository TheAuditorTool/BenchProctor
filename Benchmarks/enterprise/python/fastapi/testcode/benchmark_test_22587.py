# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from pydantic import BaseModel
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest22587(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
