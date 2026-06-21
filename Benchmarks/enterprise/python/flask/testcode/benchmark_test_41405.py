# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest41405():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
