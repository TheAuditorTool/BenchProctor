# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest46244():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return query_array
    data = asyncio.run(fetch_payload())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
