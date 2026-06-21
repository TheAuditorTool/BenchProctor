# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


request_state: dict[str, str] = {}

async def BenchmarkTest50259(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return {"updated": True}
