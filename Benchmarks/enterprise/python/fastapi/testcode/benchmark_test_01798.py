# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import os


def relay_value(value):
    return value

async def BenchmarkTest01798(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
