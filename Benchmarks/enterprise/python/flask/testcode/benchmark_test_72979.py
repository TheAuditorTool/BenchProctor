# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest72979():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
