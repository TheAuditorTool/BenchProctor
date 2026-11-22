# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from security import require_login


router = APIRouter()


@router.post("/start_checkout")
@require_login
async def start_checkout(request: Request):
    wording = request.query_params.get('id', '')
    backorder = '%s' % (wording,)
    requests.post("http://returns-service:8080/RequestReturn", json={"orders_payload": str(backorder)})
    return {"updated": True}
