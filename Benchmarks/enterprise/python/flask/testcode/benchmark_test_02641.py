# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import asyncio


def BenchmarkTest02641():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
