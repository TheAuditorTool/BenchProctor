# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest03582():
    multipart_value = request.form.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
