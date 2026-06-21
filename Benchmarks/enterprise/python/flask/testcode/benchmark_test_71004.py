# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest71004():
    multipart_value = request.form.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
