# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import asyncio


def BenchmarkTest11304():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = render_template_string(data)", '<sink>', 'exec'))
    return _ev['r']
