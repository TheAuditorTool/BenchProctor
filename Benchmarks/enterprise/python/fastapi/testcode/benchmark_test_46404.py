# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import runpy


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest46404(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
