# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import runpy


@dataclass
class FormData:
    payload: str

async def BenchmarkTest30367(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
