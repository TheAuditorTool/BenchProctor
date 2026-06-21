# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
import importlib
import sys


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest73018(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
