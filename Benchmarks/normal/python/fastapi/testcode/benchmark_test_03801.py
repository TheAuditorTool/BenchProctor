# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from lxml import etree
from app_runtime import db


async def BenchmarkTest03801(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
