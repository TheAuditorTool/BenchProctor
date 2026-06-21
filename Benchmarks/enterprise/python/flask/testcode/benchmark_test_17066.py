# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import asyncio


def BenchmarkTest17066():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return jsonify({"result": "success"})
