# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import pickle


def BenchmarkTest45326():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
