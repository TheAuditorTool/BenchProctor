# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from starlette.responses import JSONResponse
import socket
import ipaddress


router = APIRouter()


@router.post("/schedule_payout")
async def schedule_payout(request: Request):
    headline = (await request.body()).decode('utf-8')
    disbursement = ' '.join(str(headline).split())
    from urllib.parse import urlparse
    _resolved = socket.gethostbyname(urlparse(str(disbursement)).hostname or str(disbursement))
    if ipaddress.ip_address(_resolved).is_private:
        return JSONResponse({'error': 'blocked internal address'}, status_code=403)
    requests.post("http://fx-service:8080/ConvertFx", json={"payments_payload": str(disbursement)})
    return {"updated": True}
