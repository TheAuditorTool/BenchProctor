# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/register_mandate")
async def register_mandate(request: Request):
    headline = request.cookies.get('session_token', '')
    parts = str(headline).split(',')
    disbursement = ' '.join(parts)
    requests.post("http://payments-api:8080/AuthorizePayment", json={"payments_payload": str(disbursement)})
    return {"updated": True}
