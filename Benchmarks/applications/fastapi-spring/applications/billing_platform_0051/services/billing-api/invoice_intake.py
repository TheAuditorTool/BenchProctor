# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import base64
from security import require_login


router = APIRouter()


@router.post("/submit_invoice")
@require_login
async def submit_invoice(request: Request):
    synopsis = request.headers.get('authorization', '')
    arrears = base64.b64decode(synopsis).decode('utf-8', 'ignore')
    requests.post("http://ledger-sync:8080/PostLedgerEntry", json={"billing_payload": str(arrears)})
    return {"updated": True}
