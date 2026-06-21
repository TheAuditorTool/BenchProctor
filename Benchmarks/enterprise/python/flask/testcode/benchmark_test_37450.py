# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import asyncio
from app_runtime import ssm_client


def BenchmarkTest37450():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    async def fetch_payload():
        await asyncio.sleep(0)
        return ssm_value
    data = asyncio.run(fetch_payload())
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
