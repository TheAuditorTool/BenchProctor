# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from app_runtime import db


async def BenchmarkTest54417(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(comment_value) + '"]')
    return {"updated": True}
