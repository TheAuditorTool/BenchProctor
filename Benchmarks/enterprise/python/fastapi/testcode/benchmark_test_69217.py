# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import runpy


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest69217(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
