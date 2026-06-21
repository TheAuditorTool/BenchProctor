# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''
def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest57011(request: Request, req: UserInput):
    json_value = req.payload
    data = default_blank(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return {"updated": True}
