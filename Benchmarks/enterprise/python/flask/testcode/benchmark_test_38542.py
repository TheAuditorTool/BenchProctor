# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import asyncio


def BenchmarkTest38542():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
