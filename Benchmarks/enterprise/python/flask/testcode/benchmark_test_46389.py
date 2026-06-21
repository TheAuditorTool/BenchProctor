# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import asyncio


def BenchmarkTest46389():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile('_ev[\'r\'] = \'<script src="\' + str(data) + \'"></script>\', 200, {\'Content-Type\': \'text/html\'}', '<sink>', 'exec'))
    return _ev['r']
