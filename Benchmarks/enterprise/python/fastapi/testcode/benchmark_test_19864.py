# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest19864(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    eval(compile("conn = ldap.initialize('ldap://localhost:389')\nconn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
