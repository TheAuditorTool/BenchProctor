# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify
import asyncio


def BenchmarkTest33427():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
