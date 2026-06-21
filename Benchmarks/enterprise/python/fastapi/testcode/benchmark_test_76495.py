# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import asyncio


async def BenchmarkTest76495(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    await _evasion_task()
    return {"updated": True}
