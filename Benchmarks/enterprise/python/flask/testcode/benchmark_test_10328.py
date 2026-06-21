# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import asyncio


def BenchmarkTest10328():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = render_template_string(data)", '<sink>', 'exec'))
    return _ev['r']
