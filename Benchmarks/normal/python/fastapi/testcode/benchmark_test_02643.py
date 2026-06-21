# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest02643(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
