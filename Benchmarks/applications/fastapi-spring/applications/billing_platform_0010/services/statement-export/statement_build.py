# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/build_statement")
async def build_statement(request: Request):
    headline = (await request.form()).get('field', '')
    remittance = (lambda v: v.strip())(headline)
    requests.post("http://refund-service:8080/IssueRefund", json={"billing_payload": str(remittance)})
    return {"updated": True}
