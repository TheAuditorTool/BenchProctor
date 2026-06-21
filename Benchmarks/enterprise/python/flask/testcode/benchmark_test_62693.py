# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest62693():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
