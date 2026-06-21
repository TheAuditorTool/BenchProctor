# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest61048():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
