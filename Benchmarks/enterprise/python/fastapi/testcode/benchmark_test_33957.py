# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import subprocess


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest33957(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
