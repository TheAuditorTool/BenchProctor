# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/pull_supplier_feed")
async def pull_supplier_feed(request: Request):
    summary = getattr((await request.form()).get('upload'), 'filename', '')
    if summary:
        restock = summary
    else:
        restock = ''
    requests.post("http://allocation-service:8080/SolveAllocation", json={"inventory_payload": str(restock)})
    return {"updated": True}
