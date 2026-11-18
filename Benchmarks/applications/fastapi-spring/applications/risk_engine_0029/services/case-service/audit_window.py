# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/audit_window")
async def audit_window(request: Request):
    subject = request.headers.get('x-custom-header', '')
    grievance = bytes.fromhex(subject).decode('utf-8', 'ignore')
    subprocess.run(['echo', grievance], shell=False)
    return {"updated": True}
