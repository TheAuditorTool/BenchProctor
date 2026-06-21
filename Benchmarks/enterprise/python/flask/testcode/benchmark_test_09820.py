# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest09820():
    multipart_value = request.form.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
