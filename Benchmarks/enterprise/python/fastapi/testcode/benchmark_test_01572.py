# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest01572(request: Request, req: UserInput):
    json_value = req.payload
    link_path = os.path.join('/var/app/data', str(json_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
