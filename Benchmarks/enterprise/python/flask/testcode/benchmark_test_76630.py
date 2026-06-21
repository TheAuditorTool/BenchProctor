# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest76630():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
