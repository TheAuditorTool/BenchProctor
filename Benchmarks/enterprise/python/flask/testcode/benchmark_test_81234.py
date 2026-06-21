# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import request, jsonify
import asyncio
import socket


def BenchmarkTest81234():
    multipart_value = request.form.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
