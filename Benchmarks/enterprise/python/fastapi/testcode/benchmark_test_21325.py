# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest21325(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = coalesce_blank(xml_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
