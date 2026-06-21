# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
import requests
from flask import jsonify
import asyncio


def BenchmarkTest58065():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    async def fetch_payload():
        await asyncio.sleep(0)
        return api_value
    data = asyncio.run(fetch_payload())
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
