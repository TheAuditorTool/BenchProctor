# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from starlette.responses import JSONResponse
import socket
import ipaddress


router = APIRouter()


@router.post("/apply_macro")
async def apply_macro(request: Request):
    phrase = (await request.body()).decode('utf-8')
    inquiry = '{}'.format(phrase)
    from urllib.parse import urlparse
    _resolved = socket.gethostbyname(urlparse(str(inquiry)).hostname or str(inquiry))
    if ipaddress.ip_address(_resolved).is_private:
        return JSONResponse({'error': 'blocked internal address'}, status_code=403)
    requests.post("http://survey-service:8080/SendSurvey", json={"support_payload": str(inquiry)})
    return {"updated": True}
