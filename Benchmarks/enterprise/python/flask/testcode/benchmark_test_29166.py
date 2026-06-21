# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import jsonify
import asyncio


def BenchmarkTest29166(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
