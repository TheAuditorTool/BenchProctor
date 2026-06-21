# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest63787():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    return jsonify({'error': 'An internal error occurred'}), 500
