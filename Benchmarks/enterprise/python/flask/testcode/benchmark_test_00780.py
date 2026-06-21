# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00780():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
