# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import asyncio


def BenchmarkTest69343():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
