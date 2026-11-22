# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/validate_address")
async def validate_address(request: Request):
    citation = request.headers.get('x-custom-header', '')
    consignment = '%s' % (citation,)
    requests.post("http://shipping-api:8080/QuoteShipment", json={"shipping_payload": str(consignment)})
    return {"updated": True}
