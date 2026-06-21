# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest31046(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
