# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest59525(request: Request):
    referer_value = request.headers.get('referer', '')
    data = default_blank(referer_value)
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
