# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import runpy


@dataclass
class FormData:
    payload: str

async def BenchmarkTest00008(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
