# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import importlib
import sys


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest23627(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
