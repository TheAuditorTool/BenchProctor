# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import os


router = APIRouter()


@router.post("/open_case")
async def open_case(request: Request):
    summary = os.environ.get('RISK_INPUT_0030', '')
    grievance, _sep, _rest = str(summary).partition('\x00')
    requests.post("http://alert-triage:8080/TriageAlert", json={"risk_payload": str(grievance)})
    return {"updated": True}
