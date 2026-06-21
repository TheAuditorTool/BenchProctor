# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest07783(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<script src="\' + str(data) + \'"></script>\')', '<sink>', 'exec'))
    return _ev['r']
