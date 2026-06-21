# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import importlib
import sys


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest02245(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
