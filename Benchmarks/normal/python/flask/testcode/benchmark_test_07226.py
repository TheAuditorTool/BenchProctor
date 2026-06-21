# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
import asyncio
import pickle


def BenchmarkTest07226():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return jsonify({"result": "success"})
