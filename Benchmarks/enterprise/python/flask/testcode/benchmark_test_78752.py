# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
from flask import jsonify
import asyncio


def BenchmarkTest78752():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return argv_value
    data = asyncio.run(fetch_payload())
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
