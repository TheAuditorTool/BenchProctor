# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import asyncio


def BenchmarkTest51208():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile('_ev[\'r\'] = \'<script src="\' + str(data) + \'"></script>\', 200, {\'Content-Type\': \'text/html\'}', '<sink>', 'exec'))
    return _ev['r']
