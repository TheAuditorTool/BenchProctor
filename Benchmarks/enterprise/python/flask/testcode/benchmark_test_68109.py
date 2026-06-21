# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from Crypto.Cipher import DES


def BenchmarkTest68109():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
