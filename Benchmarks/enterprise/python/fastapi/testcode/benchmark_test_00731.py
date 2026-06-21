# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest00731(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    request.session['user'] = str(data)
    return {"updated": True}
