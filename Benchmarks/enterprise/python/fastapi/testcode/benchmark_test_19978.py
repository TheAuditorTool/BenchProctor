# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from app_runtime import db


async def BenchmarkTest19978(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    prefix = ''
    data = prefix + str(comment_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
