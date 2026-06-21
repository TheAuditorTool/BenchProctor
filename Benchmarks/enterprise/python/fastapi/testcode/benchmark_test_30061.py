# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest30061(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
