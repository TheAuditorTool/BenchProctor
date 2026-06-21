# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from pydantic import BaseModel
from types import SimpleNamespace


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest65870(request: Request, req: UserInput):
    json_value = req.payload
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
