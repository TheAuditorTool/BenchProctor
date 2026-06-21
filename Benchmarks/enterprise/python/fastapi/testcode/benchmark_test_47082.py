# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest47082(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
