# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest56408():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
