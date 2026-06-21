# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest02791():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
