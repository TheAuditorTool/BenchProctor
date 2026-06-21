# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest52704(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
