# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest04369(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
