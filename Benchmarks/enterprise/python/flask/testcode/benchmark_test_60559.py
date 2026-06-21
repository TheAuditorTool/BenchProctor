# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import asyncio


def BenchmarkTest60559():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
