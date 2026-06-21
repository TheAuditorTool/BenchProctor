# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
import asyncio


def BenchmarkTest04654():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = redirect(str(data))", '<sink>', 'exec'))
    return _ev['r']
