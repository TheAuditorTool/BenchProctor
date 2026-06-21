# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest30304():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.chmod('/var/app/data/' + str(processed), 0o777)
    return jsonify({"result": "success"})
