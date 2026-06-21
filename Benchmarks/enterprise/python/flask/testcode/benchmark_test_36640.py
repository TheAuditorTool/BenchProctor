# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import asyncio


def BenchmarkTest36640():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
