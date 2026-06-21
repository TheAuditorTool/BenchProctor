# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest08164(request: Request):
    path_value = request.path_params.get('id', '')
    data = relay_value(path_value)
    request.session['user'] = str(data)
    return {"updated": True}
