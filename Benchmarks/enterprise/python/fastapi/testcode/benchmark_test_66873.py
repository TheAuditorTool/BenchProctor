# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import json
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest66873(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return {"updated": True}
