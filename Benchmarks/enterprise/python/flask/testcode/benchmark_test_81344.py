# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def BenchmarkTest81344():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
