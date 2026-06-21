# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import asyncio


def BenchmarkTest26420():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
