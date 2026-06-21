# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest68282():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if str(processed) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
