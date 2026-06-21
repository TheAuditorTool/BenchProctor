# SPDX-License-Identifier: Apache-2.0
import yaml
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest01483():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
