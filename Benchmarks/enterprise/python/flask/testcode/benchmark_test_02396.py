# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest02396():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    return redirect(str(data))
