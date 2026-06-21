# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest77057(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
