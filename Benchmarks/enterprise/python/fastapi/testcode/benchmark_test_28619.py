# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import os


async def BenchmarkTest28619(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(env_value))
    return {"updated": True}
