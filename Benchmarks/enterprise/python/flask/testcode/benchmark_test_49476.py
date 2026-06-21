# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def BenchmarkTest49476():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
