# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest13024(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return {"updated": True}
