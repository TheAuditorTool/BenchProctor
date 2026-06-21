# SPDX-License-Identifier: Apache-2.0
import random
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest00130():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
