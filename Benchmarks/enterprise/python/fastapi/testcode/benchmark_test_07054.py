# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from app_runtime import db


async def BenchmarkTest07054(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(db_value).encode(), _parser)
    return {"updated": True}
