# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import importlib
import sys


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest30317(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % (json_value,)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
