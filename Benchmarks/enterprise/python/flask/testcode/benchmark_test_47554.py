# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import asyncio


def BenchmarkTest47554(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
