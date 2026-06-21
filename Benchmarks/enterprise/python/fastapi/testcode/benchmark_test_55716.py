# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import os
from types import SimpleNamespace


async def BenchmarkTest55716(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
