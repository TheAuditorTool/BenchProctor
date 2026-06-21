# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import runpy


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest28625(request: Request, req: UserInput):
    json_value = req.payload
    data, _sep, _rest = str(json_value).partition('\x00')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
