# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest51929(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return {"updated": True}
