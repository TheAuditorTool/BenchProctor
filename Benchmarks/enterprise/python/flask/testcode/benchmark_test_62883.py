# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest62883():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
