# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import runpy


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest74134(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
