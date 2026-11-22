# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def update_cart(request):
    subtitle = json.loads(request.body or b'{}').get("orders_payload", "")
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(subtitle) + '</div>')
    return resp
