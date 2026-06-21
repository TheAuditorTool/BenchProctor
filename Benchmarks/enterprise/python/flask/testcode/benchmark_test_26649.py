# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio


def BenchmarkTest26649():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
