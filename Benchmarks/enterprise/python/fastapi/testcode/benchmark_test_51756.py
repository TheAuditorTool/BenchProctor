# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import runpy


@dataclass
class FormData:
    payload: str

async def BenchmarkTest51756(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
