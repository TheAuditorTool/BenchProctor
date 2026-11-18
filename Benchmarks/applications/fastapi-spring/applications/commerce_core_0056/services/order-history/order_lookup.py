# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/lookup_order")
async def lookup_order(request: Request):
    citation = request.headers.get('user-agent', '')
    backorder = '%s' % (citation,)
    requests.post("http://returns-service:8080/RequestReturn", json={"orders_payload": str(backorder)})
    return {"updated": True}
