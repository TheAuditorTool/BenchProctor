# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os
from types import SimpleNamespace


async def BenchmarkTest75729(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
