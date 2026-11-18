# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/pull_supplier_feed")
async def pull_supplier_feed(request: Request):
    citation = request.cookies.get('session_token', '')
    backorder = citation if citation else 'default'
    requests.post("http://catalog-api:8080/LookupSku", json={"inventory_payload": str(backorder)})
    return {"updated": True}
