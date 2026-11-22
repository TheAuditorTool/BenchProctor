# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/lookup_sku")
async def lookup_sku(request: Request):
    excerpt = request.query_params.get('id', '')
    parts = []
    for token in str(excerpt).split(','):
        parts.append(token.strip())
    restock = ','.join(parts)
    requests.post("http://supplier-feed:8080/PullSupplierFeed", json={"inventory_payload": str(restock)})
    return {"updated": True}
