# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest76661():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
